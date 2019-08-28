import numpy as np
import cv2
from PIL import Image
import os



def detection(frame, faceCascade, eyesCascade, LISTE):
    
    #Config for face detection
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=3.0,#pyramid scale
        minNeighbors=1,#min number of detection for keep this detec
        minSize=(60, 100),#min size of our detection
        flags=cv2.CASCADE_SCALE_IMAGE#for old cascade
    )
    
    for x1, y1, w1, h1 in faces:#our points detected
        
        y1 = y1.tolist()#transform array to int
        y1 = y1 + 20#we down the detection face (eyes are detecting in)
        h1 = h1.tolist()#corner bot right to int
        h1 = int(round(h1/2.3))#up the detection frame

        roi_gray = frame[y1:y1+h1, x1:x1+w1]#our area detected

        cv2.rectangle(frame, (x1,y1), (x1+w1, y1+h1), 2)#draw the rectangle
        
        eyes = eyesCascade.detectMultiScale(
            roi_gray,#place of detecte our eyes
            scaleFactor=1.6,#pyramid scale (it take RAM !!)
            minNeighbors=1,#min detections for keep it
            minSize=(40, 40),#min are
            flags=cv2.CASCADE_SCALE_IMAGE#old haar
        )


        essais1(eyes, roi_gray, frame, LISTE)#Call the function who say if
                                             #the positionning




def essais1(eyes, roi_gray, frame, LISTE):

    #Sometimes eyes are superimposed
    eye = 0
    
    #Sometimes eyes switch so we initialize a count
    compteur = 0
    #left eyes
    gauche = 0
    #right eye
    droite = 0
    #if go right i must go left we cancel it (movement head)
    ok = ""

    #false detection are cancel
    if 1 < len(eyes) <= 2:
        #for points in detection
        for x, y, w, h in eyes:
            #Sometimes eyes are superimposed so we increment eye
            #from the first loop
            #if the second detecting or loop
            #is == to the first we cancel it
            if x + 5 >= eye <= x - 5:
                eye += x

                #first eye is decteting on a white frame
                if compteur == 0:
                    cv2.rectangle(roi_gray, (x,y), (x+w, y+h),(255), 2)
                    gauche = y

                #first eye is decteting on a black frame
                else:
                    cv2.rectangle(roi_gray, (x,y), (x+w, y+h),(0), 2)
                    droite = y

            #increment count or the eye
            compteur += 1

    #nothing is matched
    if gauche != 0 or droite != 0:
        #if right - 20 < left < right -5
        #left eye is highter than right eye
        if droite - 20 < gauche < droite - 5:
            print("gauche")
            ok = True#cancel the retourn of head

        if ok != True:
            #if right + 15 < left < right + 5
            #left eye is not highter than right eye
            if droite + 15 > gauche > droite + 5:
                print("droite")

    #show our draw
    cv2.imshow('VIDEO', frame)


