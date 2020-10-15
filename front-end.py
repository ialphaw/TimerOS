import time

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

from activity import reqActivity


class Manager(ScreenManager):
    m2 = ObjectProperty(None)

    req = ' '
    timex = 1

    def info(self):
        self.req = self.m1.reqText.text
        self.timex = int(self.m1.timeText.text)

        print(self.req)
        print(self.timex)

    def test(self, args):
        if self.timex > 0:
            self.timex -= 1
        else:
            self.m1.btn()
        self.m2.timer.text = f'Your Computer Will Be {self.req} In {self.timex} Seconds'
        time.sleep(1)


class Main(Screen):
    reqText = ObjectProperty(None)
    timeText = ObjectProperty(None)

    def btn(self):
        reqActivity(self.reqText, self.timeText)


class Second(Screen):
    # TODO: set the MDLabel into an timer

    pass


class MyLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        return Builder.load_file('main.kv')


MainApp().run()
