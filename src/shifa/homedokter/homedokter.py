from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition

Builder.load_file('shifa/homedokter/homedokter.kv')

class HomedokterWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_signin(self):
        self.parent.parent.transition = SlideTransition()
        self.parent.parent.switch_to(self.parent.parent.parent.ids.scrn_si, direction='right')

class HomedokterApp(App):

    def build(self):
        Window.size = (1280, 720)
        return HomedokterWindow()

if __name__ == '__main__':
    HomedokterApp().run()
