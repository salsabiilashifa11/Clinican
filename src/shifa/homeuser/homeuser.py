from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition

Builder.load_file('shifa/homeuser/homeuser.kv')

class HomeuserWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = ''
        self.idakun = -1

    def to_signin(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_si, direction='right')

    def to_pembelian(self):
        self.parent.parent.parent.ids.scrn_pb.children[0].username = self.username
        self.parent.parent.parent.ids.scrn_pb.children[0].idakun = self.idakun
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_pb, direction='left')

class HomeuserApp(App):

    def build(self):
        Window.size = (1280, 720)
        return HomeuserWindow()

if __name__ == '__main__':
    HomeuserApp().run()
