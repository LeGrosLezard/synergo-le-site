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
HAND = []
MOUVEMENT = [0]


l = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
l10 = []
l11 = []
l12 = []
l13 = []
l14 = []
l15 = []

ll1 = [[], [], [], []]
ll2 = [[], [], [], []]
ll3 = [[], [], [], []]
ll4 = [[], [], [], []]
ll5 = [[], [], [], []]
ll6 = [[], [], [], []]
ll7 = [[], [], [], []]
ll8 = [[], [], [], []]
ll9 = [[], [], [], []]
ll10 = [[], [], [], []]
ll11 = [[], [], [], []]
ll12 = [[], [], [], []]
ll13 = [[], [], [], []]
ll14 = [[], [], [], []]
ll15 = [[], [], [], []]

LOWER = []
UPPER = []





cap=cv2.VideoCapture("VIDEO.mp4")
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")


counter = 0
kernel_blur=13
seuil=10
surface=1000

hand_detection = False


while True:

    
    ret, frame =cap.read()
    frame = cv2.resize(frame, (800, 600))
    frame_movement = cv2.resize(frame, (800, 600))
    frame_area = cv2.resize(frame, (800, 600))
    

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    originale, kernel_dilate = original_traitement(cap, kernel_blur)
    contours, frame_contour = to_mask(frame_movement, gray, originale, kernel_blur, seuil, kernel_dilate)
    x_mov, y_mov, w_mov, h_mov, taille_area = contour(frame_movement, contours, surface, frame_contour)

    
    
    
    try:
        frame1, x, y, w, h = face_detector(faceCascade, gray, frame)


        if MOUVEMENT[-1] > x + 5 or MOUVEMENT[-1] < x - 5:
            ll = [[], [], [], []]
            ll1 = [[], [], [], []]
            ll2 = [[], [], [], []]
            ll3 = [[], [], [], []]
            ll4 = [[], [], [], []]
            ll5 = [[], [], [], []]
            ll6 = [[], [], [], []]
            ll7 = [[], [], [], []]
            ll8 = [[], [], [], []]
            ll9 = [[], [], [], []]
            ll10 = [[], [], [], []]
            ll11 = [[], [], [], []]
            ll12 = [[], [], [], []]
            ll13 = [[], [], [], []]
            ll14 = [[], [], [], []]
            ll15 = [[], [], [], []]
            ll16 = [[], [], [], []]
            ll17 = [[], [], [], []]


        if len(ll1[0]) < 2:
            init_zones(x, y, w, h, frame_movement,
                       ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8,
                       ll9, ll10, ll11, ll12, ll13, ll14, ll15)

        if counter == 5:
            UPPER, LOWER = most_pixel(counter, frame1)


        if counter > 5:
            skinMask, hand_detection = skin_mask(frame, frame1, frame_movement, UPPER, LOWER,
                                                 counter, x, y, w, h,
                                                 x_mov, y_mov, w_mov, h_mov, taille_area,
                                                 DIRECTION_VERTICALE, HAND,
                                                 hand_detection)
    except:
        pass




    if len(ll1[0]) >= 2:

        zones_area(frame_movement,
              ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8,
              ll9, ll10, ll11, ll12, ll13, ll14, ll15)





    MOUVEMENT.append(x)




    
    originale = gray
    cv2.imshow("frame_movement", frame_movement)
    
    counter+=1
        


    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break




cap.release()
cv2.destroyAllWindows()
