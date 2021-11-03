from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kaki.app import App
from kivy.properties import ObjectProperty


class WindowManager(ScreenManager):
    pass

class MainApp(MDApp):
    dataEncode = ObjectProperty(None)

    def build(self):
        self.title='Kriptografi'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepPurple"
        Builder.load_file("main.kv")
        return WindowManager()

    def fungsiEncode(self):
        print("test")
        # self.hasilEncode.text = self.dataEncode.text


if __name__ == "__main__":
    MainApp().run()


