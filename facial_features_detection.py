import cv2
import matplotlib.pyplot as plt


face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_smile.xml")

def detect(gray,frame):
    face=face_cascade.detectMultiScale(gray,1.5,5)
    for (x,y,w,h) in face:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),3)
        gray_roi=gray[y:y+h,x:x+w]
        color_roi=frame[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(gray_roi,1.4,22)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(color_roi,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)
    
        smile=smile_cascade.detectMultiScale(gray_roi,1.7,25)

        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(color_roi,(sx,sy),(sx+sw,sy+sh),(0,0,255),3)
      
    return frame

cap=cv2.VideoCapture(0)
while True:
  ret,frame=cap.read()
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  canvas=detect(gray,frame)
  cv2.imshow("frame",canvas)
  if cv2.waitKey(10) & 0xFF==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
