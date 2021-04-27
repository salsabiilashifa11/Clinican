from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
import mysql.connector
Builder.load_file('adila/payment.kv')

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shifawidyo", #Isi ini sama password kalian masing-masing yaa
            database="RPL"
        )
class PaymentWindow(BoxLayout):
    def __init__(self, **kwargs):
        self.username = ''
        self.idakun = -1
        self.idtransaksi = 2
        self.transaksi = []
        super().__init__(**kwargs)

    def totalHarga(_totalharga):
        total = 0
        for i in range(len(_totalharga)):
            total += _totalharga[i][7]  # bagian array yang berisi subtotal harga
        return total

    def fetch_trans(self):
        mycursor = mydb.cursor()
        query = "select IdTransaksi, IdAkun, obat.IdObat, NamaObat, Kuantitas, Stok, Harga, HargaKumu from pembelian natural inner join obat where idakun='{0}' and idtransaksi='{1}'".format(self.idakun, self.idtransaksi)
        print(query)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        self.transaksi = myresult
        print("QUERY YANG DIAMBIL")
        #print(self.parent.parent.parent.ids.scrn_pay.children[0].ids)
        print(self.transaksi)
        #return myresult

    def afterBayar(self):
        #insert to transaksi
        for i in range (len(self.transaksi)):
            val = self.transaksi[i]
            mycursor = mydb.cursor()
            queryIN = "INSERT INTO Transaksi VALUES ({0}, {1}, {2}, {3}, {4})"\
                .format(val[0], val[1], val[2], val[4], val[7])
            queryUP = "UPDATE Obat SET Stok = Stok - {0} WHERE idObat = {1}"\
                .format(val[4], val[2])
            mycursor.execute(queryIN)
            mycursor.execute(queryUP)
            mydb.commit()
            print("successfully inserted to Transaksi, updated stokObat, deleted from Pembelian")


    def delete_transaksi(self):
        for i in range (len(self.transaksi)):
            val = self.transaksi[i]
            mycursor = mydb.cursor()
            query = "DELETE FROM Pembelian WHERE IdTransaksi = {0} AND IdAkun = {1} AND IdObat = {2}"\
                .format(val[0], val[1], val[2])
            print(query)
            mycursor.execute(query)

            mydb.commit()

            print("successfully deleted record")
    
    def updateStokObat(self):
        for i in range (len(self.transaksi)):
            kuantitas = self.transaksi[i][4]
            idobat = self.transaksi[i][2]
            mycursor = mydb.cursor()
            query = "UPDATE Obat SET Stok = Stok - {0} WHERE idObat = {1}"\
                .format(kuantitas, idobat)
            print(query)
            mycursor.execute(query)
            mydb.commit()
            print("successfully updated record")


    def spinner_clicked(self, value):
        self.ids.click_label.text = f'Metode yang Anda pilih: {value}'
    
    def updateDisplay(self):
        total = 0
        for i in range (len(self.transaksi)):
            # no
            no = "no" + str(i+1)
            self.parent.children[0].ids[no].text = str(i+1)
            # barang
            barang = "barang" + str(i+1)
            self.parent.children[0].ids[barang].text = self.transaksi[i][3]
            # harga
            harga = "harga" + str(i+1)
            self.parent.children[0].ids[harga].text = str(self.transaksi[i][6])
            # jumlah
            jumlah = "jumlah" + str(i+1)
            self.parent.children[0].ids[jumlah].text = str(self.transaksi[i][4])
            # subtotal
            subtotal = "subtotal" + str(i+1)
            self.parent.children[0].ids[subtotal].text = str(self.transaksi[i][7])
            total += self.transaksi[i][7]
        self.parent.children[0].ids["totalharga"].text = str(total)

    def to_paySuccess(self):
        payS = self.parent.parent.parent.ids.scrn_payS.children[0]
        payS.username = self.username
        payS.idakun = self.idakun
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_payS, direction='left')
        payS.fetch_receipt()
        print(payS.receipt)
    
    def to_pembelian(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_pb, direction='right')
    

class PayApp(App):
    def build(self):
        Window.size = (1280, 720)
        return PaymentWindow()

if __name__ == '__main__':
    PayApp().run()

