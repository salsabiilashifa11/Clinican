from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition

Builder.load_file('shifa/homeapoteker/homeapoteker.kv')

class HomeapotekerWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_signupdokter(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_sud, direction='left')

    def to_signupapoteker(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_sua, direction='left')

    def to_signin(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_si, direction='right')

    def to_CekPembelian(self):
        self.parent.parent.transition = NoTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_cekbeli)

class HomeapotekerApp(App):

    def build(self):
        Window.size = (1280, 720)
        return HomeapotekerWindow()

if __name__ == '__main__':
    HomeapotekerApp().run()