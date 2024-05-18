import mediapipe as mp
import numpy as np
import cv2 as cv
import threading
# Mediapipe Models
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
rcounter = 0 
rstage = None
lcounter = 0 
lstage = None
# Function to Determine Angle
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
class VideoCamera():
     def __init__(self):
          self.video = cv.VideoCapture(0)
          (self.ret, self.frame) = self.video.read()
          threading.Thread(target=self.update, args=()).start()

     def __del__(self):
          self.video.release()
    
     def detected_frame(self):
          ans = DetectPose(self.frame)
          image = bicepCurls(ans)
          _, jpeg = cv.imencode('.jpg', image)
          return jpeg.tobytes()
     
     def update(self):
         while True:
             (self.ret, self.frame) = self.video.read() 

#To Yeild Result Frame Content
def gen(camera): 
    while True:
        frame = camera.detected_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Model to Predict Pose
def DetectPose(frame):
    #Convert from BGR to RGB
    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image.flags.writeable = False
    
    # Make detection
    results = pose.process(image)

    # Convert from RGB to BGR
    image.flags.writeable = True
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    landmarks = results.pose_landmarks.landmark
    pose_landmarks = results.pose_landmarks
    return landmarks, pose_landmarks, image

def bicepCurls(landmarks,pose_landmarks, image):
  try:
    Right_Shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
    Right_Elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
    Right_Wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                
    Left_Shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    Left_Elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    Left_Wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                
    # Calculate angle
    Right_Arm_Angle = calculate_angle(Right_Shoulder, Right_Elbow, Right_Wrist)
    Left_Arm_Angle = calculate_angle(Left_Shoulder, Left_Elbow, Left_Wrist)
    
    # Visualize angle
    cv.putText(image, str(Right_Arm_Angle), tuple(np.multiply(Right_Elbow, [640, 480]).astype(int)), 
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA)          
    cv.putText(image, str(Left_Arm_Angle), tuple(np.multiply(Left_Elbow, [640, 480]).astype(int)), 
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA)
    
    #Curl Counter
    if Right_Arm_Angle > 160:
            rstage = "down"
    if Right_Arm_Angle < 30 and rstage =='down':
            rstage="up"
            rcounter +=1
    if Left_Arm_Angle > 160:
            lstage = "down"
    if Left_Arm_Angle < 30 and lstage =='down':
            lstage="up"
            lcounter +=1               
  except:
        pass
                    
  cv.rectangle(image, (0,0), (100,75), (0,0,0), -1)
            
  cv.putText(image, 'RH REPS', (15,12), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
  cv.putText(image, str(rcounter), (30,60), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)
            
  cv.rectangle(image, (740,0), (900,75), (0,0,0), -1)
            
  cv.putText(image, 'LH REPS', (760,12), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
  cv.putText(image, str(lcounter), (765,60), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)

  mp_drawing.draw_landmarks(image, pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    ) 
  return image

            
            

        
       