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

SUBSTRACTOR2 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

SUBSTRACTOR3 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


SUBSTRACTOR4 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


SUBSTRACTOR5 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

SUBSTRACTOR6 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

SUBSTRACTOR7 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

SUBSTRACTOR8 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


SUBSTRACTOR9 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


SUBSTRACTOR10 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

SUBSTRACTOR11 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

SUBSTRACTOR12 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


SUBSTRACTOR13 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)


SUBSTRACTOR14 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)



def video_capture_visage():


    video = cv2.VideoCapture("video_jb.mp4")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    
    MOUVEMENT = []
    c = 0
    l = []
    c1 = 0
    l1 = []
    c2 = 0
    l2 = []
    c3 = 0
    l3 = []
    c4 = 0
    l4 = []
    c5 = 0
    l5 = []
    c6 = 0
    l6 = []
    c7 = 0
    l7 = []
    c8 = 0
    l8 = []
    c9 = 0
    l9 = []
    c10 = 0
    l10 = []
    c11 = 0
    l11 = []
    c12 = 0
    l12 = []
    c13 = 0
    l13 = []
    c14 = 0
    l14 = []

    
    
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
            
            #cv2.rectangle(gray, (x, y), (x+w, y +h), 2)
            #---------------------------------------------------------1

        


            #---------------------------------------------------------milieu

            #milieu
            cv2.rectangle(gray, (x + int(round(w/3)), y - int(round(150 * 100 / h))), (x + int(round(w/3)) * 2, y - int(round(80 * 100 / h))), (255), 2)
            crop = gray[y - int(round(150 * 100 / h)):y - int(round(80 * 100 / h)), x + int(round(w/3)):x + int(round(w/3)) * 2]
            mask = SUBSTRACTOR.apply(crop)


            liste = []

            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c = 0
                l = []

            elif c > 5:
                if sum(l) > 1000000:
                    print("milieu")

            else:
                c += 1
                l.append(sum(liste))
                
            #---------------------------------------------------------milieu
                
            #---------------------------------------------------------pattes


                
            #pattes
            #cv2.rectangle(gray, (x - 20, y - int(round(110 * 100 / h))), (x + 30, y - int(round(50 * 100 / h))), (255), 2)
            crop1 = gray[y - int(round(110 * 100 / h)):y - int(round(50 * 100 / h)), x - 20:x + 30]
            mask = SUBSTRACTOR1.apply(crop1)
            liste = []

            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c1 = 0
                l1 = []

            elif c1 > 5:
                if sum(l1) > 1000000:
                    print("patte1")


            else:
                c1 += 1
                l1.append(sum(liste))



            #cv2.rectangle(gray, (x + w - 20, y - int(round(100 * 100 / h))), (x + w + 30, y - int(round(40 * 100 / h))), (255), 2)
            crop2 = gray[y - int(round(100 * 100 / h)):y - int(round(40 * 100 / h)), x + w - 20:x + w + 30]
            mask = SUBSTRACTOR2.apply(crop2)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c2 = 0
                l2 = []

            elif c2 > 5:
                if sum(l2) > 1000000:
                    print("patte2")

            else:
                c2 += 1
                l2.append(sum(liste))

                
            #---------------------------------------------------------pattes
            #---------------------------------------------------------téco

            #téco
            #cv2.rectangle(gray, (x - w - 30, y), (x - 60, y + h - 30), 3)
            crop3 = gray[y:y + h - 30, x - w - 30:x - 60]
            mask = SUBSTRACTOR3.apply(crop3)
            
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c3 = 0
                l3 = []

            elif c3 > 5:
                if sum(l3) > 1000000:
                    print("téco1")

            else:
                c3 += 1
                l3.append(sum(liste))



            
            #cv2.rectangle(gray, (x + w + 60, y), (x + w * 2 + 30, y + h - 30), 3)
            crop4 = gray[y:y + h - 30, x + w + 60:x + w * 2 + 30]
            mask = SUBSTRACTOR4.apply(crop4)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c4 = 0
                l4 = []

            elif c4 > 5:
                if sum(l4) > 1000000:
                    print("téco2")

            else:
                c4 += 1
                l4.append(sum(liste))

            #---------------------------------------------------------téco

            #---------------------------------------------------------chebou
            #cv2.rectangle(gray,(x + int(round(w/3)), y + h - 20), (x + int(round(w/3)) * 2, y + h - 5), 1)
            crop5 = gray[y + h - 20:y + h + 10,x + int(round(w/3)):x + int(round(w/3)) * 2]
            mask = SUBSTRACTOR5.apply(crop5)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c5 = 0
                l5 = []

            elif c5 > 5:
                if sum(l5) > 1000000:
                    print("chebou")

            else:
                c5 += 1
                l5.append(sum(liste))

            #---------------------------------------------------------chebou

            #---------------------------------------------------------menton
            #cv2.rectangle(gray,(x + int(round(w/3)), y + h + 10), (x + int(round(w/3)) * 2, y + h + 25), 1)
            
            crop6 = gray[y + h + 10:y + h + 25,x + int(round(w/3)):x + int(round(w/3)) * 2]
            mask = SUBSTRACTOR6.apply(crop6)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c6 = 0
                l6 = []

            elif c6 > 5:
                if sum(l6) > 1000000:
                    print("menton")

            else:
                c6 += 1
                l6.append(sum(liste))


            #---------------------------------------------------------menton



            #---------------------------------------------------------buste
            #cv2.rectangle(gray,(x, y + h + 120), (x + w, y + h + 180), 1)

            crop7 = gray[y + h + 120:y + h + 180, x:x + w]
            mask = SUBSTRACTOR7.apply(crop7)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c7 = 0
                l7 = []

            elif c7 > 5:
                if sum(l7) > 1000000:
                    print("buste")

            else:
                c7 += 1
                l7.append(sum(liste))


            
            #---------------------------------------------------------buste


            #---------------------------------------------------------epaul
            #cv2.rectangle(gray, (x - 50, y + h + 20), (x + 30, y + h + 60), 1)


            crop8 = gray[y + h + 20:y + h + 60, x - 50:x + 30]
            mask = SUBSTRACTOR8.apply(crop8)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c8 = 0
                l8 = []

            elif c8 > 5:
                if sum(l8) > 1000000:
                    print("epaul1")

            else:
                c8 += 1
                l8.append(sum(liste))



            
            #cv2.rectangle(gray,(x + w - 30, y + h + 20), (x + w + 30, y + h + 60), 1)


            crop9 = gray[y + h + 20:y + h + 60, x + w - 30:(x + w + 30)]
            mask = SUBSTRACTOR9.apply(crop9)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c9 = 0
                l9 = []

            elif c9 > 5:
                if sum(l9) > 1000000:
                    print("epaul2")

            else:
                c9 += 1
                l9.append(sum(liste))










            
            #---------------------------------------------------------epaul


            #---------------------------------------------------------front
            #cv2.rectangle(gray, (x + 30, y - int(round(30 * 100 / h))), (x + w - 30, y - int(round(-40 * 100 / h))), 2)

            crop10 = gray[y - int(round(30 * 100 / h)):y - int(round(-40 * 100 / h)), x + 30:x + w - 30]

            mask = SUBSTRACTOR10.apply(crop10)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c10 = 0
                l10 = []

            elif c10 > 5:
                if sum(l10) > 1000000:
                    print("front")

            else:
                c10 += 1
                l10.append(sum(liste))


            
            #---------------------------------------------------------front


            #---------------------------------------------------------tempes
            cv2.rectangle(gray,(x-40, y - 20), (x, y + 40), (0), 1)

            crop11 = gray[y - 20:y + 40, x - 40:x]


            
            mask = SUBSTRACTOR11.apply(crop11)
            liste = []
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c11 = 0
                l11 = []

            elif c11 > 5:
                if sum(l11) > 1000000:
                    print("tempes1111111111111111111111")

            else:
                c11 += 1
                l11.append(sum(liste))

            

            
            cv2.rectangle(gray,(x + w, y -20), (x + w + 40, y + 40),(255), 1)

            crop12 = gray[y - 20:y + 40, x + w:x + w + 40]
           
            
            mask = SUBSTRACTOR12.apply(crop12)
            
            liste = []

      
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c12 = 0
                l12 = []

            elif c12 > 5:
                if sum(l12) > 1000000:
                    print("tempes22222")
  
            else:
                c12 += 1
                l12.append(sum(liste))


    

            


            
            #---------------------------------------------------------tempes


            #---------------------------------------------------------oreille
            cv2.rectangle(gray,(x - 40, y + 70), (x, y + 110), 1)


            crop13 = gray[y + 70:y + 110, x - 40:x]
           
        
            mask = SUBSTRACTOR13.apply(crop13)
            
            liste = []

      
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c13 = 0
                l13 = []

            elif c13 > 5:
                if sum(l13) > 1000000:
                    print("oreille1")
      
            else:
                c13 += 1
                l13.append(sum(liste))





            
            cv2.rectangle(gray,(x + w + 40, y + 70), (x + w, y + 110), 1)



            crop14 = gray[y + 70:y + 110, x + w:x + w + 40]
            
            mask = SUBSTRACTOR14.apply(crop14)
            
            liste = []

      
            for i in mask:
                for j in i:
                    liste.append(j)

            if sum(liste) == 0:
                c14 = 0
                l14 = []

            elif c14 > 5:
                if sum(l14) > 1000000:
                    print("oreille2")
          
            else:
                c14 += 1
                l14.append(sum(liste))

 



            
            #---------------------------------------------------------oreille


                    
                        
           














        #-------------------------------------------------------------1

            
  

        cv2.imshow('FACE', gray)
        

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        if len(MOUVEMENT) > 10:
            del MOUVEMENT[:8]


    video.release()
    cv2.destroyAllWindows()



video_capture_visage()






























        
