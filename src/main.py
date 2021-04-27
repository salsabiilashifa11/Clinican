"""
This module runs the main program
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from shifa.signin.signin import SigninWindow
from shifa.signindokter.signindokter import SigninDokterWindow
from shifa.signinapoteker.signinapoteker import SigninApotekerWindow
from shifa.signup.signup import SignupWindow
from shifa.signupdokter.signupdokter import SignupdokterWindow
from shifa.signupapoteker.signupapoteker import SignupapotekerWindow
from shifa.homeuser.homeuser import HomeuserWindow
from shifa.homedokter.homedokter import HomedokterWindow
from shifa.homeapoteker.homeapoteker import HomeapotekerWindow
from detha.pembelian.pembelian import PembelianWindow
from adila.paySuccess import paySuccessWindow
from adila.payment import PaymentWindow
from aisha.pembelianapoteker.pembelianapoteker import PembelianapotekerWindow

class MainWindow(BoxLayout):
    """This is the main window"""
    signin_screen = SigninWindow()
    signindokter_screen = SigninDokterWindow()
    signinapoteker_screen = SigninApotekerWindow()
    signup_screen = SignupWindow()
    signupdokter_screen = SignupdokterWindow()
    signupapoteker_screen = SignupapotekerWindow()
    homeuser_screen = HomeuserWindow()
    homedokter_screen = HomedokterWindow()
    homeapoteker_screen = HomeapotekerWindow()
    pembelian_screen = PembelianWindow()
    payment_screen = PaymentWindow()
    paySuccess_screen = paySuccessWindow()
    pembelian_apo_screen = PembelianapotekerWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scrn_si.add_widget(self.signin_screen)
        self.ids.scrn_sid.add_widget(self.signindokter_screen)
        self.ids.scrn_sia.add_widget(self.signinapoteker_screen)
        self.ids.scrn_su.add_widget(self.signup_screen)
        self.ids.scrn_sud.add_widget(self.signupdokter_screen)
        self.ids.scrn_sua.add_widget(self.signupapoteker_screen)
        self.ids.scrn_hu.add_widget(self.homeuser_screen)
        self.ids.scrn_hd.add_widget(self.homedokter_screen)
        self.ids.scrn_ha.add_widget(self.homeapoteker_screen)
        self.ids.scrn_pb.add_widget(self.pembelian_screen)
        self.ids.scrn_pay.add_widget(self.payment_screen)
        self.ids.scrn_payS.add_widget(self.paySuccess_screen)
        self.ids.scrn_cekbeli.add_widget(self.pembelian_apo_screen)


class MainApp(App):
    """This is the main app"""
    def build(self):
        Window.size = (1280, 720)
        return MainWindow()

if __name__ == '__main__':
    MainApp().run()
