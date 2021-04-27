from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
from kivy.uix.popup import Popup
import mysql.connector
import itertools

Builder.load_file('detha/pembelian/pembelian.kv')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shifawidyo", #Isi ini sama password kalian masing-masing yaa
    database="RPL"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT NamaObat from Obat limit 10")
result = mycursor.fetchall()
namaObat = list(itertools.chain(*result))
        
mycursor.execute("SELECT Stok from Obat limit 10")
result = mycursor.fetchall()
stok = list(itertools.chain(*result))

mycursor.execute("SELECT Harga from Obat limit 10")
result = mycursor.fetchall()
harga = list(itertools.chain(*result))

mycursor.execute("SELECT PictObat from Obat limit 10")
result = mycursor.fetchall()
pictObat = list(itertools.chain(*result))

mycursor.execute("SELECT Deskripsi from Obat limit 10")
result = mycursor.fetchall()
deskripsi = list(itertools.chain(*result))


def getIdTransaksi(num):
    return num + 1

def getTotalQuantity(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

class PopupObat(FloatLayout):
    #kelas untuk menampilkan pop up deskripsi obat
    def __init__(self,num,pembelianscrn,**kwargs):
        self.name = namaObat[num]
        self.pic = pictObat[num]
        self.desc = deskripsi[num]
        self.pembelianscrn = pembelianscrn
        super(PopupObat, self).__init__(**kwargs)
        pass

    def closePopup(self):
        #menutup pop up
        self.pembelianscrn.closePopup()
    pass

class PopupInfo(FloatLayout):
    #kelas untuk menampilkan pop up info pembelian
    def __init__(self,pembelianscrn,**kwargs):
        self.pembelianscrn = pembelianscrn
        self.receipt = pembelianscrn.getReceipt()
        super(PopupInfo, self).__init__(**kwargs)
    
    def closePopup(self):
        #menutup pop up
        self.pembelianscrn.closePopup()
    pass

class EmptyStock(FloatLayout):
    #kelas untuk menampilkan message box ketika stok tidak mencukupi
    def __init__(self, pembelianscrn, **kwargs):
        self.pembelianscrn = pembelianscrn
        super().__init__(**kwargs)

    def closePopup(self):
        #menutup pop up
        self.pembelianscrn.closePopup()
    pass

class EmptyKeranjang(FloatLayout):
    #kelas untuk menampilkan message box ketika keranjang belanja kosong
    def __init__(self,text, pembelianscrn,**kwargs):
        self.text = text
        self.pembelianscrn = pembelianscrn
        super(EmptyKeranjang, self).__init__(**kwargs)
    
    def closePopup(self):
        #menutup pop up
        self.pembelianscrn.closePopup()
    pass

class Confirmation(FloatLayout):
    def __init__(self, pembelianscrn, **kwargs):
        self.pembelianscrn = pembelianscrn
        super().__init__(**kwargs)

    #kelas untuk menampilkan message box konfirmasi untuk melanjutkan ke pembayaran
    def to_payment(self):
        #switch page ke PaymentWindow dan memanggil insertToDatabase()
        self.pembelianscrn.to_payment()

    def closePopup(self):
        #menutup pop up
        self.pembelianscrn.closePopup()
    pass

class PembelianWindow(BoxLayout):
    #kelas utama yang menampilkan page pembelian
    def __init__(self, **kwargs):
        self.arrName = namaObat
        self.arrStok = stok
        self.arrHarga = harga
        self.arrPict = pictObat
        self.arrDesc = deskripsi
        self.username = ""
        self.idakun = 0
        self.idtransaksi = 0
        self.msgBox = Popup()
        super().__init__(**kwargs)
        
    def changeQuantity(self, opr, num):
        #mengubah kuantitas apabila button tambah atau button kurang diklik
        if (num == 1):
            before = int(self.ids.quantity1.text)        
            if opr == '+':
                if (before == self.arrStok[0]):
                    self.showMsg()
                    return
                self.ids.quantity1.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity1.text = str(before-1)
        elif (num == 2):
            before = int(self.ids.quantity2.text)        
            if opr == '+':
                if (before == self.arrStok[1]):
                    self.showMsg()
                    return
                self.ids.quantity2.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity2.text = str(before-1)
        elif (num == 3):
            before = int(self.ids.quantity3.text)        
            if opr == '+':
                if (before == self.arrStok[2]):
                    self.showMsg()
                    return
                self.ids.quantity3.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity3.text = str(before-1)
        elif (num == 4):
            before = int(self.ids.quantity4.text)        
            if opr == '+':
                if (before == self.arrStok[3]):
                    self.showMsg()
                    return
                self.ids.quantity4.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity4.text = str(before-1)
        elif (num == 5):
            before = int(self.ids.quantity5.text)        
            if opr == '+':
                if (before == self.arrStok[4]):
                    self.showMsg()
                    return
                self.ids.quantity5.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity5.text = str(before-1)
        elif (num == 6):
            before = int(self.ids.quantity6.text)        
            if opr == '+':
                if (before == self.arrStok[5]):
                    self.showMsg()
                    return
                self.ids.quantity6.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity6.text = str(before-1)
        elif (num == 7):
            before = int(self.ids.quantity7.text)        
            if opr == '+':
                if (before == self.arrStok[6]):
                    self.showMsg()
                    return
                self.ids.quantity7.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity7.text = str(before-1)
        elif (num == 8):
            before = int(self.ids.quantity8.text)    
            if opr == '+':
                if (before == self.arrStok[7]):
                    self.showMsg()
                    return  
                self.ids.quantity8.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity8.text = str(before-1)
        elif (num == 9):
            before = int(self.ids.quantity9.text) 
            if opr == '+':
                if (before == self.arrStok[8]):
                    self.showMsg()
                    return
                self.ids.quantity9.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity9.text = str(before-1)
        elif (num == 10):
            before = int(self.ids.quantity10.text)  
            if opr == '+':
                if (before == self.arrStok[9]):
                    self.showMsg()
                    return
                self.ids.quantity10.text = str(before+1)
            else: #opr == '-' 
                if before > 0:
                    self.ids.quantity10.text = str(before-1)
    
    def showMsg(self):
        #menampilkan message box untuk menyatakan stok tidak cukup
        self.msgBox = Popup(title = "Message", title_size='16', separator_height='0',content = EmptyStock(self), size_hint=(None,None),size=(300,200))
        self.msgBox.open()
        
    def showMsg2(self):
        #menampilkan message box untuk menyatakan isi keranjang masih kosong
        self.msgBox = Popup(title = "Message", title_size='16', separator_height='0', content = EmptyKeranjang("Tidak ada obat yang dimasukkan ke dalam keranjang.",self), size_hint=(None,None),size=(500,200))
        self.msgBox.open()

    def showMsg3(self):
        #menampilkan message box untuk menyatakan isi keranjang masih kosong
        self.msgBox = Popup(title = "Message", title_size='16', separator_height='0', content = EmptyKeranjang("Silakan pilih obat yang hendak dibeli terlebih dahulu.",self), size_hint=(None,None),size=(500,200))
        self.msgBox.open()

    def showKonfirmasi(self):
        #menampilkan popup window yang meminta konfirmasi pengguna untuk melanjutkan ke pembayaran
        thisconf = Confirmation(self)
        self.msgBox = Popup(title = "Message", title_size='16', separator_height='0',content = thisconf, size_hint=(None,None),size=(400,200))
        self.msgBox.open()

    def closePopup(self):
        self.msgBox.dismiss()

    def showInfo(self):
        #menampilkan popup window berupa info pembelian
        popup = PopupInfo(self)
        self.msgBox = Popup(title = "INFO PEMBELIAN", content = popup, size_hint=(None,None),size=(500,400))
        self.msgBox.open()

    def showObat(self,num):
        #menampilkan popup window PopupObat
        popup = PopupObat(num,self)
        self.msgBox = Popup(title = "INFO " + popup.name, content = popup, size_hint=(None,None),size=(500,600)) 
        self.msgBox.open()
      
    def getArrQuantity(self):
        #mendapatkan array yang berisi kuantitas dari masing-masing obat yang hendak dibeli
        arr = [0 for i in range(10)]
        arr[0] = int(self.ids.quantity1.text)
        arr[1] = int(self.ids.quantity2.text)
        arr[2] = int(self.ids.quantity3.text)
        arr[3] = int(self.ids.quantity4.text)
        arr[4] = int(self.ids.quantity5.text)
        arr[5] = int(self.ids.quantity6.text)
        arr[6] = int(self.ids.quantity7.text)
        arr[7] = int(self.ids.quantity8.text)
        arr[8] = int(self.ids.quantity9.text)
        arr[9] = int(self.ids.quantity10.text)
        return arr
    
    def getReceipt(self):
        #men-generate struk pembayaran sementara
        sum = 0
        arrQuantity = self.getArrQuantity()
        receipt = ""
        for i in range(10):
            if arrQuantity[i] != 0:
                receipt += namaObat[i] + " " + str(harga[i]) + " x " + str(arrQuantity[i]) + "  = Rp. " + str(arrQuantity[i]*harga[i]) + "\n"
                sum += arrQuantity[i]*harga[i]
        receipt+="\nTOTAL HARGA SEMENTARA = Rp. " + str(sum)
        return receipt

    def infoPembelian(self):
        #menampilkan info pembelian 
        arrQuantity = self.getArrQuantity()
        count = 0
        for i in range(10):
            count+=arrQuantity[i]
        if (count==0):
            self.showMsg2()
            return
        self.showInfo()

    def lanjutBayar(self):
        #memeriksa apakah perlu melanjut ke page pembayaran
        arrQuantity = self.getArrQuantity()
        count = 0
        for i in range(10):
            count+=arrQuantity[i]
        if (count==0):
            self.showMsg3()
            return
        self.showKonfirmasi()

    def to_homeuser(self):
        #switch page ke HomeuserWindow
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_hu, direction='right')

    def to_payment(self):
        # switch page ke PaymentWindow dan memanggil insertToDatabase()
        self.insertToDatabase()
        pembayaranwindow = self.parent.parent.parent.ids.scrn_pay.children[0]
        pembayaranwindow.username = self.username
        pembayaranwindow.idakun = self.idakun
        pembayaranwindow.idtransaksi = self.idtransaksi
        pembayaranwindow.fetch_trans()
        pembayaranwindow.updateDisplay()
        self.parent.parent.transition = SlideTransition()
        pembayaranwindow.ids.idField.text = str(self.idtransaksi)
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_pay, direction='left')

    def insertToDatabase(self):
        #memasukkan data pembelian ke dalam database
        id = self.createIdTransaksi()
        arr = self.getArrQuantity()
        for i in range(10):
            if arr[i] != 0:
                query = "INSERT INTO Pembelian VALUES({0},{1},{2},{3},{4})"\
                    .format(id, self.idakun, i+1, arr[i], arr[i]*self.arrHarga[i])
                print(query)
                mycursor.execute(query)
        mydb.commit()

    def createIdTransaksi(self):
        #men-generate id transaksi
        mycursor.execute("SELECT MAX(IdTransaksi) FROM Pembelian")
        myresult = mycursor.fetchall()
        self.idtransaksi = self.getIdTransaksi(int(myresult[0][0]))
        return self.idtransaksi

    def getIdTransaksi(self,num):
        return num+1


class PembelianApp(App):
    def build(self):
        Window.size = (1280, 720)
        return PembelianWindow()
    
if __name__ == '__main__':
    PembelianApp().run()


