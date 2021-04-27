from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
import mysql.connector
import hashlib

Builder.load_file('shifa/signupapoteker/signupapoteker.kv')
mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shifawidyo", #Isi ini sama password kalian masing-masing yaa
            database="RPL"
        )
class SignupapotekerWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_account(self):
        nama = self.ids.name_field.text
        email = self.ids.email_field.text
        notelp = self.ids.phone_field.text
        username = self.ids.username_field.text
        password = self.ids.pass_field.text.rstrip()
        #hash password
        password = hashlib.sha256(password.encode()).hexdigest()

        #Fetch account with same username
        result = self.fetch_account(username)

        #Update message box
        message_box = self.ids.message
        if (username == '' or password == '' or nama == ''\
                or email == '' or notelp == ''):
            message_box.text = '[color=#FF0000]Please fill in all boxes[/color]'
        elif (len(result) != 0):
            message_box.text = '[color=#FF0000]Username taken! Please choose another one[/color]'
        elif (not self.is_valid_phone(notelp)):
            message_box.text = '[color=#FF0000]Invalid phone number! Only numbers allowed[/color]'
        else:
            #generate new id
            id = self.create_id()

            #insert new account
            val = (id, nama, email, notelp, username, password)
            self.insert_account(val)
            message_box.text = '[color=#26AE4C]Sign up successful![/color]'


    def fetch_account(self, _username):

        val = (_username.rstrip())
        mycursor = mydb.cursor()
        query = "SELECT * FROM Apoteker WHERE username='{0}'".format(val)
        print(query)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        print(myresult)

        return myresult

    def is_valid_phone(self, _phone_number):
        for char in _phone_number:
            if (ord(char) < 48 or ord(char) > 57):
                return False
        return True

    def create_id(self):
        mycursor = mydb.cursor()
        query = "SELECT MAX(IdApoteker) FROM Apoteker"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        print(myresult)

        return int(myresult[0][0])+1

    def insert_account(self, val):
        mycursor = mydb.cursor()
        query = "INSERT INTO Apoteker VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')"\
            .format(val[0], val[1], val[2], val[3], val[4], val[5])
        print(query)
        mycursor.execute(query)

        mydb.commit()

        print("successfully inserted record")

    def to_homeapoteker(self):
        self.ids.name_field.text = ''
        self.ids.email_field.text = ''
        self.ids.phone_field.text = ''
        self.ids.username_field.text = ''
        self.ids.pass_field.text = ''
        self.ids.message.text = ''
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_ha, direction='right')

class SignupapotekerApp(App):

    def build(self):
        Window.size = (1280, 720)
        return SignupapotekerWindow()

if __name__ == '__main__':
    SignupapotekerApp().run()

