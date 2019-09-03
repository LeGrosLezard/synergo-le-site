import os
import sys
import time
import numpy as np
import cv2
from PIL import Image
import operator
from collections import defaultdict
from essais6 import *


cap=cv2.VideoCapture("VIDEO.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

counter = 0
kernel_blur=43
seuil=10
surface=3000




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
                                 x_mov, y_mov, w_mov, h_mov, localisation)
            
            cv2.imshow("frame1", skinMask)
    except:
        pass





    #le but c de définir ou est la main mtn




    originale = gray
    cv2.imshow("frame", frame_movement)
    counter+=1
        


    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
