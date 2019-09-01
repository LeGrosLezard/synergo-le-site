import numpy as np
import cv2

def detection_faces(frame, faceCascade, gray):
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if faces == ():
        faces = (0,0,0,0)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

        #coupe image axe tete, ENFACE VENTRE
        cv2.rectangle(frame, (x-10, y), (x+w+10, y+h+800), (0, 255, 0), 2)
        mask_colonne = frame[y:y+h+800, x-50:x+w+50]

        return mask_colonne, y, y+h+800, x-50, x+w+50, faces
    
    return 0,0,0,0



def zone2(frame):
    
    #coupe l'image de 70% de haut
    cv2.rectangle(frame, (0, int(round(600*70/100))), (800, 600), (0, 255, 255), 2)
    mask = frame[int(round(600*70/100)):600, 0:800]

    return mask, int(round(600*70/100)), 600, 0, 800


def zone_extra_hemi_espace(frame, faces):

    #droite gauche du cadre
    for x, y, w, h in faces:
        cv2.rectangle(frame, (0, 0), (x, y+800), (255, 0, 0), 2)
        cv2.rectangle(frame, (x + w, 0), (x+800, y+800), (255, 0, 0), 2)

        return 0,0, x, y+800, x+w, 0, x+800, y+800







