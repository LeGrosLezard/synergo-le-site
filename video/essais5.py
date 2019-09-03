import os
import sys
import time
import numpy as np
import cv2
from PIL import Image
import operator
from collections import defaultdict
from essais6 import *



DIRECTION_VERTICALE = []
DIRECTION_HORIZONTALE = []
MOUVEMENT = []

SUBSTRACTOR9 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

l9 = []
ll9 = [[], [], [], []]






cap=cv2.VideoCapture("VIDEO.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

counter = 0
kernel_blur=43
seuil=10
surface=1000




while True:
    
    ret, frame =cap.read()
    frame = cv2.resize(frame, (800, 600))
    frame_movement = cv2.resize(frame, (800, 600))

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    originale, kernel_dilate = original_traitement(cap, kernel_blur)
    contours, frame_contour = to_mask(frame_movement, gray, originale, kernel_blur, seuil, kernel_dilate)
    x_mov, y_mov, w_mov, h_mov, localisation = contour(frame_movement, contours, surface, frame_contour)

    
    
    
    try:
        frame1, x, y, w, h = face_detector(faceCascade, gray, frame)

        if counter == 5:
            UPPER, LOWER = most_pixel(counter, frame1)

        if counter > 5:
            skinMask = skin_mask(frame, frame1, frame_movement, UPPER, LOWER, counter, x, y, w, h,
                                 x_mov, y_mov, w_mov, h_mov, localisation,
                                 DIRECTION_VERTICALE, DIRECTION_HORIZONTALE)

    except:
        pass



    #ICI les zones de la tete
    #LE BUT c de:
    #- voir ou la main va, si pres de la tete verifier angle du cadre


    originale = gray
    cv2.imshow("frame", frame_movement)
    counter+=1
        


    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
