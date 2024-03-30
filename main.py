from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from ui.user_interface import RootWidget


Builder.load_file("./ui/frontend.kv")

class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()