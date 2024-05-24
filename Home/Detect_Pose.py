# Importing Packages
import cv2 as cv
import threading
import numpy as np
from . import MP_Models


# Calculate Angle
def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    if angle >180.0:
        angle = 360-angle
    return angle 

# Video Camera Class
class VideoCamera(object):
    
    def __init__(self):
        self.video = cv.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self,code):
            code = int(code)
            print(code)
            image,value= MP_Models.bicepCurls(self.frame)
            if(code==1):
                 image, value = MP_Models.bicepCurls(self.frame)
                 print("Bicep")
            elif(code==2):
                 image, value = MP_Models.shoulderPress(self.frame)
                 print("SHoulder")
            elif(code==3):
                 image, value = MP_Models.squat(self.frame) 
                 print("Squat")
            print("______")
            print(image.shape[1],image.shape[0])
            print("______")
       
            _, jpeg = cv.imencode('.jpg', image)
            return jpeg.tobytes(), value

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

#Generate Feed 
def gen(camera, code): 
    while True:
        frame, value = camera.get_frame(code)
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

