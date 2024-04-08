from kivy.uix.screenmanager import ScreenManager, Screen
import time

class RootWidget(ScreenManager):
    pass


class StartScreen(Screen):

    def start_camera(self):
        self.manager.current = "camera_screen"


class CameraScreen(Screen):

    def start_camera(self):
        self.ids.webcam.play = True
        self.ids.webcam.texture = self.ids.webcam._camera.texture
        self.ids.camera_button.text = "Stop Camera"

    
    def stop_camera(self):
        self.ids.webcam.play = False
        self.ids.webcam.texture = None
        self.ids.camera_button.text = "Turn Camera On"
        self.manager.current = "start_screen"

    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        image_path = f"assets/{current_time}.png"
        self.ids.webcam.export_to_png(image_path)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.current_image.source = image_path


class ImageScreen(Screen):

    def create_link(self):
        

    def copy_link(self):
        pass

    def share(self):
        pass

    def reset(self):
        self.manager.current = "camera_screen"