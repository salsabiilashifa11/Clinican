from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.app import runTouchApp
import kivy.uix.widget
import mysql.connector
import itertools

Builder.load_file('aisha/pembelianapoteker/pembelianapoteker.kv')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shifawidyo",
    database="RPL"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT IdObat from Obat limit 10")
result = mycursor.fetchall()
idObat_o = list(itertools.chain(*result))

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

mycursor.execute("SELECT idTransaksi from Transaksi limit 10")
result = mycursor.fetchall()
idTransaksi = list(itertools.chain(*result))

mycursor.execute("SELECT idAkun from Transaksi limit 10")
result = mycursor.fetchall()
idAkun_t = list(itertools.chain(*result))

mycursor.execute("SELECT idObat from Transaksi limit 10")
result = mycursor.fetchall()
idObat_t = list(itertools.chain(*result))

mycursor.execute("SELECT Kuantitas from Transaksi limit 10")
result = mycursor.fetchall()
kuantitas = list(itertools.chain(*result))

mycursor.execute("SELECT HargaKumu from Transaksi limit 10")
result = mycursor.fetchall()
harga_kumu = list(itertools.chain(*result))



def KuantitasPerObat():
    kuantitas_obat = []
    for i in range (len(idObat_o)):
        totalObat = 0
        for j in range (len(idObat_t)):
            if (idObat_o[i] == idObat_t[j]):
                totalObat += kuantitas[j]
        kuantitas_obat.append(totalObat)
    return kuantitas_obat

def PemasukanPerObat(kuantitas_obat):
    pemasukan_obat = []
    for i in range (len(idObat_o)):
        pemasukan_obat.append(harga[i]*kuantitas_obat[i])
    return pemasukan_obat

def searchNamaObat(id_):
    for i in range (len(namaObat)):
        if (idObat_o[i] == id_):
            return namaObat[i]
    return "Tidak di kenali"

kuantitas_per_obat = KuantitasPerObat()
pemasukan_per_obat = PemasukanPerObat(kuantitas_per_obat)

def toString(arr):
    list_string = []
    for angka in arr:
        list_string.append(str(angka))
    return list_string

class PopupDetailPembelian(FloatLayout):
    #kelas untuk menampilkan pop up info pembelian
    def __init__(self, idx, **kwargs):
        if (idx < len(idTransaksi) and idx >= 0):
            self.idTrans = str(idTransaksi[idx - 1])
            self.idAkun = str(idAkun_t[idx - 1])
            self.namaObat = searchNamaObat(idObat_t[idx - 1])
            self.kuantitas = str(kuantitas[idx - 1])
            self.harga = str(harga_kumu[idx - 1])
        else:
            self.idTrans = " "
            self.idAkun = " "
            self.namaObat = " "
            self.kuantitas = " "
            self.harga = " "
        super(PopupDetailPembelian, self).__init__(**kwargs)
    pass

class PopupStokObat(FloatLayout):
    def __init__(self,**kwargs):
        self.idObat = idObat_o
        self.name = namaObat
        self.stok = stok
        super(PopupStokObat, self).__init__(**kwargs)
        pass
    def getidObat(self,idx):
        return str(self.idObat[idx])
    def getNamaObat(self,idx):
        return self.name[idx]
    def getStok(self,idx):
        return str(self.stok[idx])

class PopupPemasukan(FloatLayout):
    def __init__ba(self,**kwargs):
        self.idObat = idObat_o
        self.name = namaObat
        self.kuantitas = KuantitasPerObat()
        self.pemasukanObat = PemasukanPerObat(self.kuantitas)

        super(PopupPemasukan, self).__init__(**kwargs)
        pass

    def getidObat(self,idx):
        return str(idObat_o[idx])
    def getNamaObat(self,idx):
        return namaObat[idx]
    def getKuantitas(self,idx):
        return str(KuantitasPerObat()[idx])
    def getPemasukanObat(self,idx):
        return str(PemasukanPerObat(KuantitasPerObat())[idx])
    def totalPemasukan(self):
        sum = 0
        for harga in PemasukanPerObat(KuantitasPerObat()):
            sum += harga
        return str(sum)

class PembelianapotekerWindow(BoxLayout):

    def __init__(self, **kwargs):
        self.Arr_idObat_o = idObat_o
        self.Arr_namaObat = namaObat
        self.Arr_stok = stok
        self.Arr_harga = harga
        self.Arr_idTransaksi = idTransaksi
        self.Arr_idAkun_t = idAkun_t
        self.Arr_idObat_t = idObat_t
        self.Arr_kuantitas = kuantitas
        self.Arr_harga_kumu = harga_kumu
        super().__init__(**kwargs)
    def showCekBeli(self,idx):
        #menampilkan popup window PopupInfo()
        popup = PopupDetailPembelian(idx)
        infoWindow = Popup(title = "DETAIL PEMBELIAN", content = popup, size_hint=(.5,.7), background_color=(0,0,0,0))
        infoWindow.open()
    
    def ShowStokObat(self):
        popup = PopupStokObat()
        infoWindow = Popup(title = "STOK OBAT", content = popup, size_hint=(.5,.7), background_color=(0,0,0,0))
        infoWindow.open()

    def ShowPemasukan(self):
        popup = PopupPemasukan()
        infoWindow = Popup(title = "DETAIL PEMASUKAN", content = popup, size_hint=(.5,.7), background_color=(0,0,0,0))
        infoWindow.open()

    def to_homeapoteker(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_ha, direction='right')
        


class PembelianapotekerApp(App):

    def build(self):
        Window.size = (1280, 720)
        return PembelianapotekerWindow()



if __name__ == '__main__':
    PembelianapotekerApp().run()


