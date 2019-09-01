import numpy as np
import cv2
import time
from PIL import Image
import operator
from collections import defaultdict

#Nous détectons la tete.
#par la tete nous pourrons construire nos régions.
#Nous pouvons aussi récupérer la couleur de sa figure.

#A quoi servent nos régions ?
#Les régions vont servir à localiser les grands mouvements.

#Les grands mouvements ?
#Les grands mouvements sont les mouvements de bras
#par ces grands mouvements nous pourront détecter les mains.


def detection_faces(frame, faceCascade, gray):
    
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
        detect_color(x, y, w, h, frame)
        
        return faces

    return 0, 0, 0, 0


def detect_color(x, y, w, h, frame):
    if x != 0 and y != 0 and w != 0:
        frame = frame[y+10:y+h-10, x+30:x+w-35]

        dico = {}
        img = Image.fromarray(frame)
        for value in img.getdata():
            if value in dico.keys():
                dico[value] += 1
            else:
                dico[value] = 1
                
        sorted_x = sorted(dico.items(), key=operator.itemgetter(1), reverse=True)
        print(sorted_x)
        
        cv2.imshow("ddd", frame)

        """Ne pas le faire de suite, le faire 5 fois"""

    return True

def region():
    pass

def aire_contour(aire, frame, x, y, w, h, face):
    proba = 0

    if aire > 30000:
        cv2.putText(frame, str("Grand Mouvement "  + "" + str(proba) + " %"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

    else:
        cv2.putText(frame, str("Petit Mouvement "  + "" + str(proba) + " %"), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)



def search_contour(frame_contour, frame, contours, faceCascade, gray):

    surface=3000

    
    for c in contours:
        if cv2.contourArea(c) < 100000:

            cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 5)
            if cv2.contourArea(c) < surface:
                continue
            faces = detection_faces(frame, faceCascade, gray)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            
            aire_contour(cv2.contourArea(c), frame, x, y, w, h, faces)




#UN GRAND MOUVEMENT:
            #peut etre deux mains reunis
            #peut etre une mouvement de bras.

            #si un grand mouvement se coupe en deux
                #x grand == x petit
                #y+h grand == y+h petit --> Main



#UN PETIT MOUVEMENT
            #peut etre la gueule
            #peut etre la chemise
            #peut etre les mains.

































