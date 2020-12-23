import cv2
import numpy as np
cap=cv2.VideoCapture(0)

open_kernal=np.ones((2,2),np.uint8)
close_kernal=np.ones((5,5),np.uint8)
lower_bound=np.array([7,30,80])
upper_bound=np.array([40,255,255])

black_lower_bound=np.array([0,0,0])
black_upper_bound=np.array([0,0,200])


for i in range(30):
    _,background=cap.read()

background=cv2.flip(background,1)

while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv_color=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv_color,lower_bound,upper_bound)
    #mask1=cv2.inRange(hsv_color,black_lower_bound,black_upper_bound)
    #mask=mask+mask1
    
    mask=cv2.morphologyEx(mask ,cv2.MORPH_OPEN, open_kernal,iterations=2)
    mask=cv2.morphologyEx(mask ,cv2.MORPH_CLOSE, close_kernal,iterations=4)
    mask=cv2.morphologyEx(mask ,cv2.MORPH_DILATE, close_kernal,iterations=2)
   # mask=cv2.morphologyEx(mask ,cv2.MORPH_OPEN, open_kernal,iterations=2)
    
    
    
    mask_inv=cv2.bitwise_not(mask)
    
    
    img_b=cv2.bitwise_and(background,background,mask=mask)
    img_f=cv2.bitwise_and(frame,frame,mask=mask_inv)
    final=cv2.addWeighted(img_b, 1, img_f, 1, 0)
    cv2.imshow("Invisible Cloak",final)
    cv2.imshow("hsv",hsv_color)
    cv2.imshow("mask",mask)
    cv2.imshow("Mask_inv",mask_inv)
    cv2.imshow("background",background)
    if cv2.waitKey(30) & 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
