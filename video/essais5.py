import os
import sys
import time
import numpy as np
import cv2
from PIL import Image
import operator
from collections import defaultdict

cap=cv2.VideoCapture("VIDEO.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

c = 0
a = []
b = []
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

        frame1 = frame[y+10:y+h-10, x+30:x+w-35]


        if c == 5:
            dico = {}
            img = Image.fromarray(frame1)
            for value in img.getdata():
                if value in dico.keys():
                    dico[value] += 1
                else:
                    dico[value] = 1
                    
            sorted_x = sorted(dico.items(), key=operator.itemgetter(1), reverse=True)
            print(sorted_x[0][0])
            print(sorted_x[-1][0])
            
            a = sorted_x[0][0][0]+20, sorted_x[0][0][1]+20, sorted_x[0][0][2]+20
            b = sorted_x[-1][0][0], sorted_x[-1][0][1], sorted_x[-1][0][2]

        if c > 5:
            lower = np.array([a], dtype = "uint8")
            upper = np.array([b], dtype = "uint8")
            skinMask = cv2.inRange(frame, upper, lower)
            cv2.imshow("frame1", skinMask)
        



    cv2.imshow("frame", frame)
    c+=1
        


    key=cv2.waitKey(500)&0xFF
    if key==ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
