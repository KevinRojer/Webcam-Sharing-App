import cv2

class CameraInterface:
    """
    Manages the camera's lifecycle, captures images, and provides frames for preview.
    """

    def __init__(self, camera_id, resolution, frame_rate):
        self.camera_id = camera_id
        self.resolution = resolution
        self.frame_rate = frame_rate
        self.capture = cv2.VideoCapture(0)


    def start_camera(self):
        pass


    def stop_camera(self):
        pass


    def capture(self):
        pass
