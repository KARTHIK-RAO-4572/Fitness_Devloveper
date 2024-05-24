import cv2 as cv
import mediapipe as mp
from . import Detect_Pose as dp
import numpy as np
import math

# Media Pipe Models
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose=mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

rcounter = 0 
rstage = None
lcounter = 0 
lstage = None

# Bicep Curls
def bicepCurls(frame):
        global rcounter, rstage,  lcounter, lstage 
            # Recolor image to RGB
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detection
        results = pose.process(image)
    
            # Recolor back to BGR
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        try:
            landmarks = results.pose_landmarks.landmark
                
                # Get coordinates
            Right_Shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            Right_Elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            Right_Wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                
            Left_Shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            Left_Elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            Left_Wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                
            # Calculate angle
            Right_Arm_Angle = dp.calculate_angle(Right_Shoulder, Right_Elbow, Right_Wrist)
            Left_Arm_Angle = dp.calculate_angle(Left_Shoulder, Left_Elbow, Left_Wrist)
                
            # Visualize angle
            cv.putText(image, str(Right_Arm_Angle), 
                            tuple(np.multiply(Right_Arm_Angle, [640, 480]).astype(int)), 
                            cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA
                                    )
                
            cv.putText(image, str(Left_Arm_Angle), 
                            tuple(np.multiply(Left_Arm_Angle, [640, 480]).astype(int)), 
                            cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA
                                    )
            # Curl counter logic
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
            
            # Render curl counter
            # Setup status box
        cv.rectangle(image, (0,0), (100,75), (0,0,0), -1)
            
            # Rep data
        cv.putText(image, 'RH REPS', (15,12), 
                        cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
        cv.putText(image, str(rcounter), 
                        (30,60), 
                        cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)
        
        #________________
        cv.rectangle(image, (540,0), (640,75), (0,0,0), -1)
            
            # Rep data
        cv.putText(image, 'LH REPS', (565,12), 
                        cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
        cv.putText(image, str(lcounter), 
                        (570,60), 
                        cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)
            
            
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    ) 
        return cv.resize(image, (660,520),interpolation=cv.INTER_AREA), rcounter

press_counter = 0
press_stage = None
def shoulderPress(frame):
        global press_counter, press_stage
     #Conversion
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            Left_Shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            Left_Elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            Left_Wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Calculate elbow angle
            elbow_angle = dp.calculate_angle(Left_Shoulder, Left_Elbow, Left_Wrist)

            # Compute distances between joints
            shoulder2elbow_dist = abs(math.dist(Left_Shoulder,Left_Elbow))
            shoulder2wrist_dist = abs(math.dist(Left_Shoulder,Left_Wrist))

            # Press counter logic
            if (elbow_angle > 130) and (shoulder2elbow_dist < shoulder2wrist_dist):
                press_stage = "up"
            if (elbow_angle < 50) and (shoulder2elbow_dist > shoulder2wrist_dist) and (press_stage =='up'):
                press_stage='down'
                press_counter += 1
                
            # cv.putText(image, str(elbow_angle), 
            #                tuple(np.multiply(Left_Shoulder, [640, 480]).astype(int)), 
            #                cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv.LINE_AA
            #                     )
                       
        except:
            pass
        
        cv.rectangle(image, (0,0), (100,75), (0,0,0), -1)
            
            # Rep data
        cv.putText(image, 'PRESS', (15,12), 
                        cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
        cv.putText(image, str(press_counter), 
                        (30,60), 
                        cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)
        
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
        
        return cv.resize(image, (660,520),interpolation=cv.INTER_AREA), press_counter


squat_counter = 0
squat_stage = None
def get_coordinates(landmarks, mp_pose, side, joint):
    coord = getattr(mp_pose.PoseLandmark,side.upper()+"_"+joint.upper())
    x_coord_val = landmarks[coord.value].x
    y_coord_val = landmarks[coord.value].y
    return [x_coord_val, y_coord_val]  

def squat(frame):
        global squat_counter, squat_stage
     # Recolor image to RGB
        image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            left_shoulder = get_coordinates(landmarks, mp_pose, 'left', 'shoulder')
            left_hip = get_coordinates(landmarks, mp_pose, 'left', 'hip')
            left_knee = get_coordinates(landmarks, mp_pose, 'left', 'knee')
            left_ankle = get_coordinates(landmarks, mp_pose, 'left', 'ankle')
            # right side
            right_shoulder = get_coordinates(landmarks, mp_pose, 'right', 'shoulder')
            right_hip = get_coordinates(landmarks, mp_pose, 'right', 'hip')
            right_knee = get_coordinates(landmarks, mp_pose, 'right', 'knee')
            right_ankle = get_coordinates(landmarks, mp_pose, 'right', 'ankle')

            # Calculate knee angles
            left_knee_angle = dp.calculate_angle(left_hip, left_knee, left_ankle)
            right_knee_angle = dp.calculate_angle(right_hip, right_knee, right_ankle)

            # Calculate hip angles
            left_hip_angle = dp.calculate_angle(left_shoulder, left_hip, left_knee)
            right_hip_angle = dp.calculate_angle(right_shoulder, right_hip, right_knee)

            # Squat counter logic
            thr = 165
            if (left_knee_angle < thr) and (right_knee_angle < thr) and (left_hip_angle < thr) and (right_hip_angle < thr):
                squat_stage = "down"
            if (left_knee_angle > thr) and (right_knee_angle > thr) and (left_hip_angle > thr) and (right_hip_angle > thr) and (squat_stage =='down'):
                squat_stage='up'
                squat_counter += 1
                
        except:
            pass
        
        cv.rectangle(image, (0,0), (100,75), (0,0,0), -1)
            
            # Rep data
        cv.putText(image, 'SQUAT', (15,12), 
                        cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
        cv.putText(image, str(squat_counter), 
                        (30,60), 
                        cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv.LINE_AA)
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )      
        return cv.resize(image, (660,520),interpolation=cv.INTER_AREA), squat_counter

             
     
       