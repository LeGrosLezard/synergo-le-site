import numpy as np
import cv2
from PIL import Image
import os


SUBSTRACTOR = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

SUBSTRACTOR1 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


def video_capture_visage():


    video = cv2.VideoCapture("video_jb.mp4")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    MOUVEMENT = []
    c = 0
    d = []
    e = 0
    f = []
    
    
    while(True):


        ret, frame_visage = video.read()
        frame_visage = cv2.resize(frame_visage, (1200, 1000))
        frame_visage1 = cv2.resize(frame_visage, (1200, 1000))


        

        gray = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)

        #-------------------------------------------------------------1
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=3.0,
            minNeighbors=1, minSize=(60, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)

        for x, y, w, h in faces:
            
            cv2.rectangle(gray, (x, y), (x+w, y +h), 2)
            #---------------------------------------------------------2

            MOUVEMENT.append(x)

            

            try:


                #---------------------------------------------------------

                #milieu
                #cv2.rectangle(gray, (x + int(round(w/3)), y - int(round(150 * 100 / h))), (x + int(round(w/3)) * 2, y - int(round(80 * 100 / h))), 2)
                crop = gray[y - int(round(150 * 100 / h)):y - int(round(80 * 100 / h)), x + int(round(w/3)):x + int(round(w/3)) * 2]
                mask = SUBSTRACTOR.apply(crop)


                liste = []

                for i in mask:
                    for j in i:
                        liste.append(j)

                if sum(liste) == 0:
                    c = 0
                    d = []

                elif c > 5:
                    if sum(d) > 1000000:
                        #print("mouvement")
                        pass
                else:
                    c += 1
                    d.append(sum(liste))


                #pattes
                cv2.rectangle(gray, (x - 20, y - int(round(110 * 100 / h))), (x + 30, y - int(round(50 * 100 / h))), 2)
                crop1 = gray[y - int(round(110 * 100 / h)):y - int(round(50 * 100 / h)), x - 20:x + 30]
                mask = SUBSTRACTOR1.apply(crop1)
                liste1 = []

                for i in mask:
                    for j in i:
                        liste1.append(j)

                if sum(liste1) == 0:
                    e = 0
                    f = []

                elif c > 5:
                    if sum(f) > 1000000:
                        print("mouvement1")
 
                else:
                    e += 1
                    f.append(sum(liste1))




                    
                        
            except:
                pass

        #-------------------------------------------------------------1

            
  

        cv2.imshow('FACE', gray)
        

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if len(MOUVEMENT) > 10:
            del MOUVEMENT[:8]


    video.release()
    cv2.destroyAllWindows()



video_capture_visage()






























        
