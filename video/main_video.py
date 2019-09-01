import os
import sys
import time
import numpy as np
import cv2

#skin detector (visage + en dessous)

#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture("VIDEO.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

kernel_blur=43
seuil=20
#seuil=10
surface=3000
ret, originale=cap.read()
originale = cv2.resize(originale, (800, 600))
originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)
originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
kernel_dilate=np.ones((10, 10), np.uint8)


from essais1 import *

#faut stocker les carrés la dedans
LISTE = []
LISTE2 = []

while True:
    
    ret, frame=cap.read()
    frame = cv2.resize(frame, (800, 600))
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    mask_colonne, y1_col, y2_col, x1_col, x2_col, faces = detection_faces(frame, faceCascade, gray)
    mask, y1_zon, y2_zon, x1_zon, x2_zon = zone2(frame)
    x1_hemi1, y1_hemi1, x2_hemi1, y2_hemi1,\
              x1_hemi2, y1_hemi2, x2_hemi2, y2_hemi2 = zone_extra_hemi_espace(frame, faces)
    


    gray=cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
    mask=cv2.absdiff(originale, gray)
    mask=cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask=cv2.dilate(mask, kernel_dilate, iterations=5)
    contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame_contour=frame.copy()


    #print(y1_col, y2_col, x1_col, x2_col, "colonne")
    #print(y1_zon, y2_zon, x1_zon, x2_zon, "zone 2")
    #print(x1_hemi1, y1_hemi1, x2_hemi1, y2_hemi1, "DROITE")
    #print(x1_hemi2, y1_hemi2, x2_hemi2, y2_hemi2, "GAUCHE")

    compteur_rect  = 0
    for c in contours:
        if cv2.contourArea(c) < 100000:

            cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 5)
            if cv2.contourArea(c) < surface:
                continue
            
            x, y, w, h = cv2.boundingRect(c)
            possibilite_main(x, y, w, h, LISTE, cv2.contourArea(c), LISTE2)

    
            cv2.rectangle(frame, (x, y), (int(round(x+w/2)), int(round(y+h/4))), (0, 0, 255), 2)

            #cv2.putText(frame, str("main?"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
            
            
            #print(x, y, x+w, y+h, "carre")
            #print(cv2.contourArea(c), "AREA")

            """!IMPORTANT"""      
            situation_mouvement(cv2.contourArea(c),
                                x, y, y1_zon, x2_hemi1,
                                x2_hemi2, w, x1_col, x2_col, frame)

            compteur_rect += 1
            




    #print(compteur_rect, "nombre carre")

    if compteur_rect == 0:
        print("fin ici on analyse")
        LISTE2 = []
        LISTE = []
    else:  
        for i in LISTE2:
            print(i)
        print("")
        for i in LISTE:
            print(i)
        print("")
        print("")

    
    cv2.putText(frame, str(compteur_rect), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)



    
    originale = gray

    



   


    cv2.imshow("frame", frame)
    

        
    #cv2.imshow("mask", mask)
    #cv2.imshow("dazdaz", mask_colonne)


    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break



    

    if compteur_rect > 0:
        time.sleep(1)


cap.release()
cv2.destroyAllWindows()
