from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp

from timer import countdown


class Manager(ScreenManager):
    pass


class Main(Screen):
    reqText = ObjectProperty(None)
    timeText = ObjectProperty(None)

    def btn(self, args):
        countdown(int(self.timeText.text))


class Second(Screen):
    timer = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #TODO: set the MDLabel into an timer





class MyLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file('main.kv')


MainApp().run()
