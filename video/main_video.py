import numpy as np
import cv2
from PIL import Image
import os




def video_capture_visage():


    video = cv2.VideoCapture("VIDEO.mp4")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    MOUVEMENT = []
    c = 0
    
    while(True):

        ret, frame_visage = video.read()
        frame_visage = cv2.resize(frame_visage, (1200, 1000))

        gray = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)

        #-------------------------------------------------------------1
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=3.0,
            minNeighbors=1, minSize=(60, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)

        for x, y, w, h in faces:
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0,0,0), 2)
    
            #---------------------------------------------------------2

            MOUVEMENT.append(x)

            try:
                if MOUVEMENT[-2] - 10 < x > MOUVEMENT[-2] + 10:
                    print("oui")
                else:

                    #---------------------------------------------------------
                    print("non")
                    y = y - int(round(150 * 100 / h))
                    y1 = y - int(round(80 * 100 / h))
                    carre = int(round(w/3))

                    cv2.rectangle(gray, (x + carre, y), (x + carre * 2, y1), (0), 2)

                    print(y, y1, carre)

                    


















                    
            except:
                pass

        #-------------------------------------------------------------1

            
  

        cv2.imshow('FACE', gray)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if len(MOUVEMENT) > 10:
            del MOUVEMENT[:8]

        c += 1
    video.release()
    cv2.destroyAllWindows()



video_capture_visage()






























        
