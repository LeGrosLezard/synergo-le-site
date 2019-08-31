import os
import sys
import time
import numpy as np
import cv2

#skin detector (visage + en dessous)

#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("video.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

kernel_blur=43
seuil=10
#surface=15000
surface=3000
ret, originale=cap.read()
originale = cv2.resize(originale, (800, 600))
originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)
originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
kernel_dilate=np.ones((10, 10), np.uint8)


while True:
    
    ret, frame=cap.read()
    frame = cv2.resize(frame, (800, 600))
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

        
        cv2.rectangle(frame, (x-50, y), (x+w+50, y+h+800), (0, 255, 0), 2)
        mask_colonne = frame[y:y+h+800, x-50:x+w+50]


        
    gray=cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
    mask=cv2.absdiff(originale, gray)
    mask=cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask=cv2.dilate(mask, kernel_dilate, iterations=5)
    contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame_contour=frame.copy()
    
    for c in contours:
        if cv2.contourArea(c) > 100000:
            pass
        else:
            cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 5)
            if cv2.contourArea(c) < surface:
                continue
            x, y, w, h=cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            #print(x, x+w, y, y+h)


    
    
    originale=gray


    


    
    #coupe l'image de 70% de haut
    cv2.rectangle(frame, (0, int(round(600*70/100))), (800, 600), (0, 255, 255), 2)
    mask = frame[int(round(600*70/100)):600, 0:800]
    
    
    #si gros carré puis petit dans l'axe de la figure = le mec se tient les main
    #si gros carré puis 2 autres carré alors 

    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("dazdaz", mask_colonne)

    intrus=0
    key=cv2.waitKey(30)&0xFF
    if key==ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
