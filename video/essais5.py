import os
import sys
import time
import numpy as np
import cv2



cap=cv2.VideoCapture("VIDEO2.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")


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

    if faces == ():
        faces = [(0,0,0,0)]

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

    

        try:

            frame1 = frame[y+10:y+h-10, x+30:x+w-35]

            dico = {}
            img = Image.fromarray(frame)
            for value in img.getdata():
                if value in dico.keys():
                    dico[value] += 1
                else:
                    dico[value] = 1
                    
            sorted_x = sorted(dico.items(), key=operator.itemgetter(1), reverse=True)
            print(sorted_x)

        except:
            pass


        
    cv2.imshow("frame", frame)
    cv2.imshow("ddd", frame1)
        


    key=cv2.waitKey(500)&0xFF
    if key==ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
