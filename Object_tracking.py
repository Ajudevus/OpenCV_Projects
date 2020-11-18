
import numpy as np
import cv2
from collections import deque
import sys


#pts=[]
pts=deque(maxlen=100)
lower_red=np.array([110,50,50])
upper_red=np.array([130,255,255])

#fmog=cv2.createBackgroundSubtractorMOG2()
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.mp4',fourcc,24.0,(600,600))

while True:
    _,frame=cap.read()
    kernal=np.ones((5,5),np.uint8)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
    mask=cv2.inRange(hsv, lower_red ,upper_red)

    mask=cv2.erode(mask,kernal,iterations=1)
    mask=cv2.dilate(mask, kernal)
    res=cv2.bitwise_and(frame, frame,mask=mask)
    cnt,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    center=None
    if len(cnt) > 0:
       
        c=max(cnt, key=cv2.contourArea)
        M=cv2.moments(c)
    
        (x,y),radius=cv2.minEnclosingCircle(c)
         
        cv2.circle(frame,(int(x),int(y)),int(radius),(0,0,255),-1)
        center=(int(x),int(y))
        print(pts)
        print(len(pts))
         
   
    #pts.append(center)    
    pts.appendleft(center)
    for i in range(1,len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue
        thick=int(np.sqrt(len(pts)//(i+1))*5)
        cv2.line(frame, pts[i-1], pts[i], (0,0,255),thick)
    out.write(frame)    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


    
      
      
