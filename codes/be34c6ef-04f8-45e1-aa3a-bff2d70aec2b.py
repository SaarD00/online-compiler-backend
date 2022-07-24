import cv2
cap = cv2.VideoCapture(0)
import mediapipe as mp
import pyautogui

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
palm_y = 0
middle_y = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands: 
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landsmarks = hand.landmark
            for id, landmark in enumerate(landsmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)

                # For mouse movement
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)

                # for click

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < 50:
                        pyautogui.click()
                   

               

                # # scroll

                # if id == 1: 
                #      cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                #      palm_x = screen_width/frame_width*x
                #      palm_y = screen_height/frame_height*y
                #      print("palm is", abs(palm_y - screen_height))
                #      if abs(palm_y - screen_height) > 500:
                #         pyautogui.scroll(100, palm_x, palm_y)
               

               # RIGHT CLICK FUNCTIONS --------------------------------
               
                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if abs(middle_y - thumb_y) < 50:
                        print(middle_y - thumb_y)
                        pyautogui.rightClick()
                        


    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)