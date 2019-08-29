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
        thresh = cv2.threshold(gray, 130, 255, 1)[1]

        #-------------------------------------------------------------1
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=3.0,
            minNeighbors=1, minSize=(60, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)

        for x, y, w, h in faces:
            
    
            #---------------------------------------------------------2

            MOUVEMENT.append(x)



            try:
                if MOUVEMENT[-2] - 10 < x > MOUVEMENT[-2] + 10:
                    print("oui")
                else:

                    #---------------------------------------------------------

                    def coloriage(a, b, c, d):
                        for i in range(a, b):
                            for j in range(c, d):
                                thresh[i ,j] = 255

                    #milieu
                    cv2.rectangle(thresh, (x + int(round(w/3)), y - int(round(150 * 100 / h))), (x + int(round(w/3)) * 2, y - int(round(80 * 100 / h))), 2)
                    coloriage(y - int(round(150 * 100 / h)), y - int(round(80 * 100 / h)), x + int(round(w/3)),x + int(round(w/3)) * 2)






                    
                    #pattes
                    cv2.rectangle(thresh, (x - 20, y - int(round(110 * 100 / h))), (x + 30, y - int(round(50 * 100 / h))), 2)
                    coloriage(y - int(round(110 * 100 / h)), y - int(round(50 * 100 / h)), x - 20, x + 30)

                    
                    cv2.rectangle(thresh, (x + w - 20, y - int(round(100 * 100 / h))), (x + w + 30, y - int(round(40 * 100 / h))), 2)
                    coloriage(y - int(round(100 * 100 / h)), y - int(round(40 * 100 / h)), x + w - 20, x + w + 30)
                            
                    #téco
                    cv2.rectangle(gray, (x - w - 30, y), (x - 60, y + h - 30), 3)
                    coloriage(y, y + h - 30, x - w - 30, x - 60)
                    cv2.rectangle(gray, (x + w + 60, y), (x + w * 2 + 30, y + h - 30), 3)
                    coloriage(y, y + h - 30, x + w + 60, x + w * 2 + 30)

                            
                    #chebou
                    cv2.rectangle(gray,(x + int(round(w/3)), y + h - 20), (x + int(round(w/3)) * 2, y + h - 5), 1)
                    coloriage(y + h - 20, y + h - 5, x + int(round(w/3)), x + int(round(w/3)) * 2)

                            
                    #menton
                    cv2.rectangle(gray,(x + int(round(w/3)), y + h + 10), (x + int(round(w/3)) * 2, y + h + 25), 1)
                    coloriage(y + h + 10, y + h + 25, x + int(round(w/3)), x + int(round(w/3)) * 2)

                            
                    #buste
                    cv2.rectangle(gray,(x, y + h + 120), (x + w, y + h + 180), 1)
                    coloriage(y + h + 120, y + h + 180, x, x + w)

                            
                    #epaul
                    cv2.rectangle(gray, (x - 50, y + h + 20), (x + 30, y + h + 60), 1)
                    coloriage(y + h + 20, y + h + 60, x - 50, x + 30)
                    
                    cv2.rectangle(gray,(x + w - 30, y + h + 20), (x + w + 30, y + h + 60), 1)
                    coloriage(y + h + 20, y + h + 60, x + w - 30,x + w + 30)
                            
                    #front
                    cv2.rectangle(gray, (x + 30, y - int(round(30 * 100 / h))), (x + w - 30, y - int(round(-40 * 100 / h))), 2)
                    coloriage(y - int(round(30 * 100 / h)), y - int(round(-40 * 100 / h)), x + 30, x + w - 30)
                            
                    #tempes
                    cv2.rectangle(gray,(x - 40, y - 20), (x, y + 40), 1)
                    coloriage(y - 20, y + 40, x - 40, x)
                    
                    cv2.rectangle(gray,(x + w, y + 40), (x + w + 40, y - 20 ), 1)
                    coloriage(y + 40, y - 20, x + w, x + w + 40)

                    cv2.rectangle(gray,(x - 40, y + 70), (x, y + 110), 1)
                    coloriage(y + 70, y + 110, x - 40, x)

                    
                    cv2.rectangle(gray,(x + w + 40, y + 70), (x + w, y + 110), 1)
                    coloriage(y + 70, y + 110, x + w + 40, x + w)
                    
                        
            except:
                pass

        #-------------------------------------------------------------1

            
  

        cv2.imshow('FACE', thresh)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if len(MOUVEMENT) > 10:
            del MOUVEMENT[:8]

        c += 1
    video.release()
    cv2.destroyAllWindows()



video_capture_visage()






























        
