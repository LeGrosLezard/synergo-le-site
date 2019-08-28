import numpy as np
import cv2
from PIL import Image
import os
import time

from traitement_video import detection


def video_capture_tete():

    video = cv2.VideoCapture("video2.mp4")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    #Initializing time to 0
    timer = 0
    
    while(True):
        no_timer = False
        out = ""
        
        start_time = time.time()
        
        ret, frame = video.read()
        frame = cv2.resize(frame, (1200, 1000))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        pos = detection(frame, faceCascade, eyesCascade)
        
        if pos is not None:
            timer += (time.time() - start_time)
            left = "à " + str(round(timer * 10)) + "la tete pencge à " + pos + "la personne se met à la place du téléspectateur, il invoque sa sensibilité"
            right "à " + str(round(timer * 10)) + "la tete pencge à " + pos + "la personne raisonne, la personne analyse ? faut speech recognition"

            if pos == "gauche":
                out = left
                print(left)
            elif pos == "droite":
                out = right
                print(right)

            #with open("", "a") as file:
                #file.write(out)


            no_timer = True

            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.imshow('VIDEO', frame)

        if no_timer is None:
            timer += (time.time() - start_time)
        
    video.release()
    cv2.destroyAllWindows()



video_capture_tete()


















