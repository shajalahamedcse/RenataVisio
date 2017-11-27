import cv2
import threading
import time

class CapturingThread (threading.Thread):
    def __init__(self, name, camera,na):
        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = True

        self.cap = camera
        success, image = self.cap.read()
        time.sleep(0.1)  # If you don't wait, the image will be dark
        
        cv2.imwrite(na, image)

    def stop(self):
        self.isRunning = False

    def __del__(self):
        self.out.release()


class VideoCamera(object):
    def __init__(self):
        # Open a camera
        self.cap = cv2.VideoCapture(0)
      
        # Initialize  capturing environtment
        self.is_caputred = False
        self.out = None

        # Thread for capturing
        self.capturingThread = None
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            frame=cv2.resize(frame,(500,500))
            ret, jpeg = cv2.imencode('.jpg', frame)
 

            return jpeg.tobytes()
      
        else:
            return None

    def capture(self,na):
        self.is_caputred = True
        self.capturingThread = CapturingThread("Image Capturing Thread", self.cap,na)
        self.capturingThread.start()
        self.capturingThread.stop()
        


    

        

            