import pyautogui as pyg
import numpy as np
import cv2




#defining upper and lower bound for blue color
lower_blue=np.array([88,92,21])
upper_blue=np.array([179,255,255])

cap=cv2.VideoCapture(0)
kernal=np.ones((3,3),np.uint8)

while True:
    #reading frame by frame
    _,frame=cap.read()
    #flipping the frame in horizontal axis 
    frame=cv2.flip(frame,1)
    #Converting the frame from BGR to HSV format 
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #applying thresholding
    mask=cv2.inRange(hsv, lower_blue ,upper_blue)
    #Applying filter-MORPH_OPEN(erosion followed by dilation)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal,iterations=2)
    #MORPH_CLOSE(dilation followed by dilation)
    mask=cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal,iterations=2)
    #preserving the foreground of the object
    res=cv2.bitwise_and(frame, frame,mask=mask)
    #detecting contours(points that make up edges)
    #CHAIN_APPROX_NONE detects the edge points
    cnt,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    cv2.line(frame,(225,0),(225,700),(0,255,0),4)
    cv2.line(frame,(425,0),(425,700),(0,255,0),4)
    cv2.line(frame,(225,200),(425,200),(0,255,0),4)
    
    cv2.putText(frame, "UP", (300,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.putText(frame, "DOWN", (300,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.putText(frame, "LEFT", (90,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    cv2.putText(frame, "RIGHT", (500,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
    
    
    if len(cnt) > 0:
        
        c=max(cnt, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #finding the centroid of the enclosing rectangle
        center_x,center_y=int((x+x+w)/2),int((y+y+h)/2)
        cv2.circle(frame,(center_x,center_y),2,(0,0,255),-1)        
        
        if center_x>225 and center_x<425:
            if center_y<200:
                # to fire the keyboard keys
                pyg.press("up")
                print("up")
            
            else:
                pyg.press("down")
                print("down")
        if center_x<225:
            pyg.press("left")
            print("left")
        elif center_x>425:
            pyg.press("right")
            print("right")
        
    cv2.imshow("frame",frame)
    #cv2.imshow("mask",mask)
    #cv2.imshow("res",res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


    
