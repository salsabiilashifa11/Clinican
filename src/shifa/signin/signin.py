from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
import mysql.connector
import hashlib

Builder.load_file('shifa/signin/signin.kv')
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shifawidyo", #Isi ini sama password kalian masing-masing yaa
            database="RPL"
        )
class SigninWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_account(self):
        print(self.parent.parent)
        username = self.ids.username_field.text
        password = self.ids.pass_field.text
        print(password)
        password = hashlib.sha256(password.encode()).hexdigest()
        print(password)

        #Fetch and validate
        result = self.fetch_account(username)

        message_box = self.ids.message
        if (username == '' or password == ''):
            message_box.text = '[color=#FF0000]Please fill in all boxes![/color]'
        elif (len(result) == 0):
            message_box.text = '[color=#FF0000]Username not found![/color]'
        elif (password != result[0][5]):
            message_box.text = '[color=#FF0000]Incorrect password![/color]'
        else:
            message_box.text = '[color=#000000]Sign in successful![/color]'
            self.parent.parent.parent.ids.scrn_hu.children[0].ids.name_field.text = result[0][1].upper() + '!'
            self.parent.parent.parent.ids.scrn_hu.children[0].username = username
            self.parent.parent.parent.ids.scrn_hu.children[0].idakun = result[0][0]
            self.parent.parent.parent.ids.scrn_pay.children[0].ids.name_field.text = result[0][1].upper() + '!'
            print(self.parent.parent.parent.ids.scrn_hu.children[0].idakun)
            self.reset_fields()
            self.to_homeuser()

    def fetch_account(self, _username):
       
        val = (_username.rstrip())
        mycursor = mydb.cursor()
        query = "SELECT * FROM Customer WHERE username='{0}'".format(val)
        print(query)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        print(myresult)

        return myresult

    def to_homeuser(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_hu, direction='left')

    def to_signup(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_su, direction='left')

    def to_signindokter(self):
        self.parent.parent.transition = NoTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_sid)

    def to_signinapoteker(self):
        self.parent.parent.transition = NoTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_sia)

    def verify(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def reset_fields(self):
        self.ids.username_field.text = ''
        self.ids.pass_field.text = ''
        self.ids.message.text = ''

class SigninApp(App):

    def build(self):
        Window.size = (1280, 720)
        return SigninWindow()

if __name__ == '__main__':
    SigninApp().run()