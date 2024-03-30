from kivy.uix.screenmanager import Screen

class FirstScreen(Screen):

    def search_image(self):
        self.manager.current_screen.ids.img.source = "picture.jpg"


class SecondScreen(Screen):
    pass