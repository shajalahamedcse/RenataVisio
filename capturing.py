from camera import VideoCamera
import threading
class CapturingThread (threading.Thread):
    def __init__(self, name, camera):
        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = True

        self.cap = camera
        success, image = self.cap.read()
        time.sleep(0.1)  # If you don't wait, the image will be dark
        
        cv2.imwrite("opencv.jpg", image)

    def stop(self):
        self.isRunning = False

    def __del__(self):
        self.out.release()