from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from src.screens import FirstScreen


Builder.load_file("./src/frontend.kv")


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()