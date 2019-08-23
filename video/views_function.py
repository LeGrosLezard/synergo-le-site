import cv2
import time
import os
import numpy as np
from ffpyplayer.player import MediaPlayer
import threading

PATH_VIDEO = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\synergo\media\{0}"
PATH_TEXT = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\synergo\media\texte_video\{0}"

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
    cv2.imshow('VIDEO', frame)
    time.sleep(0.05)
    
    text_video = file_name(video_name)
    with open(PATH_TEXT.format(text_video), "a") as file:
        file.write(str(message))


def video_text_(message):
    
    img = np.zeros((500,500,3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    x = 0
    fontScale = 0.5
    fontColor = (255,255,255)
    lineType = 2

    liste = []
    compteur = 0
    text = ""
    for i in message:
        for j in i:
            if compteur == 80:
                liste.append(text)
                compteur = 0
                text = ""
                

            compteur += 1
            text += j

    y = 10
    for i in liste:
        cv2.putText(img, i, (x, y), font, 
                    fontScale, fontColor, lineType)
        y += 20

    cv2.imshow("text",img)


def displaying_video_user(video_name):

    #Create video object with path video of click of user
    video = cv2.VideoCapture(PATH_VIDEO.format(video_name))
    #Sound of the video
    #sound = MediaPlayer(PATH_VIDEO.format(video_name))
    ok = True
    c = 0
    #Loop while True read this:
    while(True):

        #If key push (but it don't serve here)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            ok = False

        if cv2.waitKey(1) & 0xFF == ord('b'):
            ok = True
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

        if ok is True:
            video_capt(video, video_name, c)
            message= "bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour bonjour "
            video_text_(message)
            

        c+=1
            
    #I don't know
    video.release()
    #Destroy all windowd
    cv2.destroyAllWindows()



def recup_analysis(video_name):
    """Here we read the text
    and return it"""

    text_video = file_name(video_name)
    with open(PATH_TEXT.format(text_video), "r") as file:
        text = file.read()

    return text










