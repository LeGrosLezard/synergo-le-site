import os
import sys
import time
import numpy as np
import cv2



cap=cv2.VideoCapture("VIDEO2.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")


kernel_blur=43
seuil=10

ret, originale=cap.read()
originale = cv2.resize(originale, (800, 600))
originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)
originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
kernel_dilate=np.ones((10, 10), np.uint8)

from essais4 import search_contour

while True:
    
    ret, frame=cap.read()
    frame = cv2.resize(frame, (800, 600))
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray=cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
    
    mask=cv2.absdiff(originale, gray)
    mask=cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask=cv2.dilate(mask, kernel_dilate, iterations=5)
    contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame_contour=frame.copy()

    #on cherche les contours
    search_contour(frame_contour, frame, contours, faceCascade, gray)


    


    originale = gray


    
    
    cv2.imshow("frame", frame)

        


    key=cv2.waitKey(500)&0xFF
    if key==ord('q'):
        break




cap.release()
cv2.destroyAllWindows()


























