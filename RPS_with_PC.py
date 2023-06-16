import cv2
import mediapipe as mp
import time
import random

mp_drawing = mp.solutions.drawing_utils
mphands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mphands.Hands()

previous_time = 0
status = 0# 0 = unknown , 1 = rock , 2 = paper , 3 = scissor
confirm = 0
PC_choice = 0;
stop = 0
while True:
    data,image = cap.read()
    
    

    image = cv2.flip(image,1)
    results = hands.process(image)

    
    """
    if(results.multi_hand_landmarks):
        print(results.multi_hand_landmarks[8])
        print(results.multi_hand_landmarks[7])
    """
    current_time = time.time()
    fps = 1/(current_time-previous_time)
    previous_time = current_time
    cv2.putText(image,f'fps:{int(fps)}',(20,30),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
    cv2.putText(image,'Press f to play',(120,30),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
    if(results.multi_hand_landmarks):
        for hands_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hands_landmarks,mphands.HAND_CONNECTIONS)
            
        lmList = []
        myHand = results.multi_hand_landmarks[0]
        for id, lm in enumerate(myHand.landmark):
            # print(id, lm)
            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append([id, cx, cy])
        #print(lmList)
        print(lmList[5][2]-lmList[6][2])
        if(lmList[5][2]-lmList[6][2])<=15 and (lmList[6][2]-lmList[5][2])>=-15 and (lmList[9][2]-lmList[10][2])<=15 and (lmList[10][2]-lmList[9][2])>=-15:
            cv2.putText(image,'Rock',(20,60),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            status = 1
        elif (lmList[14][2]-lmList[15][2])>=15 and (lmList[15][2]-lmList[14][2])<=-15 :
            cv2.putText(image,'Paper',(20,60),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            status = 2
        elif (lmList[14][2]-lmList[15][2])<=15 and (lmList[15][2]-lmList[14][2])>=-15 and (lmList[5][2]-lmList[6][2])>=15 and (lmList[6][2]-lmList[5][2])<=-15 and (lmList[9][2]-lmList[10][2])>=15 and (lmList[10][2]-lmList[9][2])<=-15:
            cv2.putText(image,'Scissors',(20,60),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            status = 3
        else:
            cv2.putText(image,'Unknown',(20,60),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            status = 0
    
    
    if((cv2.waitKey(1) & 0xFF) == ord('f')):
        # 0 = unknown , 1 = rock , 2 = paper , 3 = scissor
        confirm = status
        PC_choice = random.randint(1,3)
        if(confirm == 0):
            cv2.putText(image,'Fail to determine your choice',(40,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 1 and PC_choice == 1:
            cv2.putText(image,'Draw',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Rock',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 1 and PC_choice == 2:
            cv2.putText(image,'Lose',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Paper',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 1 and PC_choice == 3:
            cv2.putText(image,'Win',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Scissors',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 2 and PC_choice == 1:
            cv2.putText(image,'Win',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Rock',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 2 and PC_choice == 2:
            cv2.putText(image,'Draw',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Paper',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 2 and PC_choice == 3:
            cv2.putText(image,'Lose',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Scissors',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 3 and PC_choice == 1:
            cv2.putText(image,'Lose',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Rock',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 3 and PC_choice == 2:
            cv2.putText(image,'Win',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Paper',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        elif confirm == 3 and PC_choice == 3:
            cv2.putText(image,'Draw',(20,90),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
            cv2.putText(image,'PC_choice:Scissors',(20,120),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1)
        if stop == 0:    
            stop = 1
    cv2.imshow("img",image)
    if stop == 1:
        stop = 0
        cv2.waitKey(5000)
    if((cv2.waitKey(1) & 0xFF) == ord('q')):
       break
cap.release()
cv2.destroyAllWindows()