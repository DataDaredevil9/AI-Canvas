import cv2
import numpy as np
import mediapipe as mp

# Capturing the video
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error: Could not open video.")
    exit()

# Initializing the Hand detector
hand_detector = mp.solutions.hands
hand = hand_detector.Hands(static_image_mode=False,max_num_hands=1,
min_detection_confidence=0.5,min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

#Storing the previous position of the index finger
prev_x, prev_y = 0, 0
#Defining the canvas for drawing
canvas = None

# -----------Drawing Tools----------
toolbar_height = 100
eraser_thickness = 50
brush_thickness = 15
drawing_color = (242, 2, 59)

colors ={
"pink" : (242, 7, 139),
"green" : (0,255,0),
"blue" : (0, 248, 255),
"yellow" : (245, 241, 42),
"eraser" : (0,0,0)
}
while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    if canvas is None:
        canvas = np.zeros_like(frame)   
    frame = cv2.flip(frame,1)
    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # ================TOOLBAR================
    cv2.rectangle(frame, (0, 0), (900, toolbar_height), (50, 50, 50), -1) 
    cv2.rectangle(frame, (20, 10), (100, 60), colors["pink"], -1) 
    cv2.rectangle(frame, (130, 10), (210, 60), colors["blue"], -1) 
    cv2.rectangle(frame, (240, 10), (320, 60), colors["green"], -1) 
    cv2.rectangle(frame, (350, 10), (430, 60), colors["yellow"], -1) 
    cv2.rectangle(frame, (460, 10), (540, 60), colors["eraser"], -1)
    cv2.putText(frame, "ERASE", (550, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    landmark_list = [] 
    result = hand.process(frame_rgb)
    if result.multi_hand_landmarks:
        for hands in result.multi_hand_landmarks:
            for index,lndmrk in enumerate(hands.landmark):
                h, w, c = frame.shape
                cx, cy = int(lndmrk.x*w), int(lndmrk.y*h)
                landmark_list.append([index,cx,cy])
                cv2.circle(frame,(cx,cy),6,(255,0,255),cv2.FILLED)
                
        #Defining the tip of the index finger
        index_up = False
        if landmark_list[8][2] < landmark_list[6][2]:
            index_up = True
        
        #Defining the tip of the middle finger
        middle_up = False
        if landmark_list[12][2] < landmark_list[10][2]:
            middle_up = True
        
        #Defining the tip of the ring finger
        ring_up = False
        if landmark_list[16][2] < landmark_list[14][2]:
            ring_up = True
        
        #Defining the tip of the small finger
        small_up = False
        if landmark_list[20][2] < landmark_list[18][2]:
            small_up = True
        
        #Defining the tip of the thumb
        thumb_up = False
        if landmark_list[4][1]  < landmark_list[3][1]:
            thumb_up = True
        
        
        
        
        #Defining the modes
        if index_up and not middle_up:
            #Drawing Mode
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = landmark_list[8][1], landmark_list[8][2]
                thickness = eraser_thickness if drawing_color == colors["eraser"] else brush_thickness
            cv2.line(canvas,(prev_x, prev_y),(landmark_list[8][1], landmark_list[8][2]),drawing_color,thickness,cv2.LINE_AA)
            prev_x, prev_y = landmark_list[8][1], landmark_list[8][2]
            cv2.putText(frame,"Drawing Mode",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,drawing_color,2)
        
        elif thumb_up and index_up and middle_up and ring_up and small_up:
            canvas = np.zeros((480,640,3),np.uint8)
            prev_x, prev_y = 0, 0
            cv2.putText(frame,"Clear Canvas",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),4)
            
        
        
        elif index_up and middle_up:
            prev_x, prev_y = 0, 0
            #Selection Mode
            if landmark_list[8][2] < toolbar_height:
                if 20 < landmark_list[8][1] < 100:
                    drawing_color = colors["pink"]
                elif 130 < landmark_list[8][1] < 210:
                    drawing_color = colors["blue"]
                elif 240 < landmark_list[8][1] < 320:
                    drawing_color = colors["green"]
                elif 350 < landmark_list[8][1] < 430:
                    drawing_color = colors["yellow"]
                elif 460 < landmark_list[8][1] < 540:
                    drawing_color = colors["eraser"]
                    thickness = eraser_thickness
            
            cv2.putText(frame,"Selection Mode",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
        
        gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
        inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

        frame = cv2.bitwise_and(frame, inv)
        frame = cv2.bitwise_or(frame, canvas)


            
    
    cv2.imshow('Hand Tracking',frame)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
