import cv2
import time
import os
import numpy as np
import threading

PATH_VIDEO = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\synergo\media\{0}"
PATH_TEXT = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\synergo\media\texte_video\{0}"
PATH_TEXT_STATIC = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\static\video_texte\{}"


def file_name(video_name):
    """We create name of our file"""

    video_name = str(video_name)
    text_video = str(video_name[13:-4]) + ".txt"

    return text_video


def video_capt(video, video_name, message):
    #Picture by picture reading
    ret, frame = video.read()
    #sound
    #audio_frame, val = sound.get_frame()
    """possibility to changes ?"""
    #frame to 400x60xx
    frame = cv2.resize(frame, (600, 400)) 
    #Displaying it
    #cv2.imshow('VIDEO', frame)

    text_video = file_name(video_name)
    with open(PATH_TEXT.format(text_video), "a") as file:
        file.write(str(message))

from .traitement_video import detection
def displaying_video_user(video_name):

    #Call function who displaying video
    video = cv2.VideoCapture(PATH_VIDEO.format(video_name))
    faceCascade = cv2.CascadeClassifier(r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\video\haarcascade_frontalface_alt2.xml")
    eyesCascade = cv2.CascadeClassifier(r'C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\video\haarcascade_eye.xml')
    
    #Initializing time to 0
    timer = 0
    LISTE = []
    path_to_text = PATH_TEXT_STATIC.format(str(video_name[13:-3]) + "txt")
    print(path_to_text)

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
            left = "<u>à " + str(round(timer * 10)) + " sec :</u> la tete penche à " + pos + " la personne se met à la place du téléspectateur, il invoque sa sensibilité\n<br>"
            right = "<u>à " + str(round(timer * 10)) + " sec :</u> la tete penche à " + pos + " la personne raisonne, la personne analyse\n<br>"

            if pos == "gauche":
                out = left
                #print(left)
            elif pos == "droite":
                out = right
                #print(right)

            #we direct write into file for template out
            with open(path_to_text, "a") as file:
                file.write(out)

            #we add it for free analysis (end of analysis)
            LISTE.append([out, timer])

            no_timer = True

            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        #cv2.imshow('VIDEO', frame)

        if no_timer is None:
            timer += (time.time() - start_time)



    video.release()
    cv2.destroyAllWindows()


def recup_analysis(video_name):
    """Here we read the text
    and return it"""


    text_video = file_name(video_name)

    with open(PATH_TEXT_STATIC.format(text_video), "r") as file:
        text = str(file.read())


    return text







