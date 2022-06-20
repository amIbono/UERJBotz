import cv2
import numpy as np

cap = cv2.VideoCapture('opencv\joevideo.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = cv2.line(frame,(0,0),(width,height),(255,0,0),10) # BLUE GREEN RED
    img = cv2.line(img,(0,height),(width,0),(0,255,0),5)
    img = cv2.rectangle(img,(100,100),(200,200),(128,128,128),5)
    img = cv2.circle(img,(300,300),60,(0,0,255),0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img,'Joe mt foda na tela',(45,height-50),font,0.8,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow('frame',img)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()