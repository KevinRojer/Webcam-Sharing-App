from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()
    


if __name__ == "__main__":
    MainApp().run()