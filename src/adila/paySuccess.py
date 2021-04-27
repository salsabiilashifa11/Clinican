from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
import mysql.connector
Builder.load_file('adila/paySuccess.kv')

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shifawidyo", #Isi ini sama password kalian masing-masing yaa
        database="RPL"
    )
        
class paySuccessWindow(BoxLayout):

    def __init__(self, **kwargs):
        
        self.username = ''
        self.idakun = -1
        self.idtransaksi = 2
        self.receipt = []
        super().__init__(**kwargs)
    
    def fetch_receipt(self):

        mycursor = mydb.cursor()
        query = "SELECT * FROM Transaksi WHERE idakun = '{0}' AND idtransaksi = '{1}'"\
            .format(self.idakun, self.idtransaksi)
        print(query)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        self.receipt = myresult

        print("QUERY YANG DIAMBIL")
        #print(self.parent.parent.parent.ids.scrn_pay.children[0].ids)
        print(self.receipt)

    def to_homeuser(self):
        self.parent.parent.transition = NoTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_hu)


class PaySApp(App):

    def build(self):
        Window.size = (1280, 720)
        return paySuccessWindow()

if __name__ == '__main__':
    PaySApp().run()
