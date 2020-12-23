import cv2
import numpy as np

def call_back():
    pass

cv2.namedWindow('color pallete')

cv2.createTrackbar('R','color pallete' , 0, 255, call_back)
cv2.createTrackbar('G','color pallete' , 0, 255, call_back)
cv2.createTrackbar('B','color pallete' , 0, 255, call_back)
cv2.createTrackbar('switch', 'color pallete', 0, 1, call_back)


img = np.zeros((320,512,3),np.uint8)

while(1):
    cv2.imshow('color pallete',img)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    r=cv2.getTrackbarPos('R', 'color pallete')
    g=cv2.getTrackbarPos('G', 'color pallete')
    b=cv2.getTrackbarPos('B', 'color pallete')
    s=cv2.getTrackbarPos('switch', 'color pallete')
    
    if s == 1:
        img[:]=[b,g,r]
    else:
        img[:]=0
    
    
    
    
cv2.destroyAllWindows()
