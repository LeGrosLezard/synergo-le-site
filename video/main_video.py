import numpy as np
import cv2
from PIL import Image
import os
import time

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

    #k, j, l <- video jb

    #for displaying video
    video = cv2.VideoCapture("l.mp4")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    
    #We croping our frame by box
    #we add content of the detection movement
    #if the sum of the list exceeds a threshold
    #there are movement
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

    
    listee = []

    #We add all detection into this list.
    #if nothing is input in there
    #we stop and run a loop for see wat detection is did
    liste_display = []
    compteur = 0
    compteur1 = 0

    
    while(True):

        
        ret, frame_visage = video.read()
        frame_visage = cv2.resize(frame_visage, (1000, 800))

        #gray for more speed
        gray = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        #face detection
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=3.0,
            minNeighbors=1, minSize=(60, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)

        #on detection
        for x, y, w, h in faces:

            
            def detection(mask, l, phrase):
                """Here we ask the sum of the list(we insert element in list
                from the box). if the mean > + 50000 there is movement in there"""
                try:
                    #doing the sum of elements of the list
                    liste = sum([j for i in mask for j in i])
                    #we add the sum of all element
                    l.append(liste)
                    #if the current list of detection is > at the mean of all passation
                    #a refaire
                    if liste > sum(l)/len(l) + 50000:
                        #we return the point detected
                        return phrase
                except:
                    pass


            #We create box. In this box we substract the current background
            #If there are movement in there the number of pixel up.
            crop3 = gray[y:y + h - 30, x - w - 30:x - 60]
            mask = SUBSTRACTOR3.apply(crop3)
            
            coté1 = detection(mask, l3, "droite")

             
            crop4 = gray[y:y + h - 30, x + w + 60:x + w * 2 + 30]
            mask = SUBSTRACTOR4.apply(crop4)
            
            coté2 = detection(mask, l4, "gauche")

            
            crop = gray[y - int(round(150 * 100 / h)):y - int(round(80 * 100 / h)), x + int(round(w/3)):x + int(round(w/3)) * 2]
            mask = SUBSTRACTOR.apply(crop)

            milieu = detection(mask, l, "milieu")

            
            crop1 = gray[y - int(round(110 * 100 / h)):y - int(round(50 * 100 / h)), x - 20:x + 30]
            mask = SUBSTRACTOR1.apply(crop1)

            patte1 = detection(mask, l1, "pate droite")

     
            crop2 = gray[y - int(round(110 * 100 / h)):y - int(round(50 * 100 / h)), x + w - 20:x + w + 30]
            mask = SUBSTRACTOR2.apply(crop2)
            
            patte2 = detection(mask, l2, "pate gauche")


            crop5 = gray[y + h - 20:y + h + 10,x + int(round(w/3)):x + int(round(w/3)) * 2]
            mask = SUBSTRACTOR5.apply(crop5)
            
            bouche = detection(mask, l5, "chebou")


            crop6 = gray[y + h + 10:y + h + 25,x + int(round(w/3)):x + int(round(w/3)) * 2]
            mask = SUBSTRACTOR6.apply(crop6)

            menton = detection(mask, l6, "menton")


            crop7 = gray[y + h + 120:y + h + 180, x:x + w]
            mask = SUBSTRACTOR7.apply(crop7)

            buste = detection(mask, l7, "buste")


            crop8 = gray[y + h + 20:y + h + 60, x - 50:x + 30]
            mask = SUBSTRACTOR8.apply(crop8)
            
            épaul1 = detection(mask, l8, "épaule droite")


            crop9 = gray[y + h + 20:y + h + 60, x + w - 30:(x + w + 30)]
            mask = SUBSTRACTOR9.apply(crop9)
            
            épaul2 = detection(mask, l9, "épaule gauche")


            crop10 = gray[y - int(round(30 * 100 / h)):y - int(round(-40 * 100 / h)), x + 30:x + w - 30]
            mask = SUBSTRACTOR10.apply(crop10)
            
            front = detection(mask, l10, "front")


            crop11 = gray[y - 20:y + 40, x - 40:x]
            mask = SUBSTRACTOR11.apply(crop11)
            
            tempe1 = detection(mask, l11, "tempe droite")
            

            crop12 = gray[y - 20:y + 40, x + w:x + w + 40]
            mask = SUBSTRACTOR12.apply(crop12)
            
            tempe2 = detection(mask, l12, "tempe gauche")

    
            crop13 = gray[y + 70:y + 110, x - 40:x]
            mask = SUBSTRACTOR13.apply(crop13)

            oreille1 = detection(mask, l13, "oreille droite")


            crop14 = gray[y + 70:y + 110, x + w:x + w + 40]
            mask = SUBSTRACTOR14.apply(crop14)

            oreille2 = detection(mask, l14, "oreille gauche")

            #for ewample for touch my forehead
            #i need to activate my shoulder to
            #pass by my hear the coin of shoulder and the shoulder.
            #so i dont touch my hear but my shoulder so shoulder == 1 and hear == 4
            if milieu:
                if coté1:
                    liste_display.append("milieu par main droite")
                else:
                    liste_display.append("milieu par main gauche")

            elif front:
                if épaul1 or épaul2:
                    if épaul1:
                        liste_display.append("front par main droite")
                        
                        
                    else:
                        liste_display.append("front par main gauche")
                else:
                    liste_display.append("front")
                    
            elif patte1 or patte2:
                if patte1:
                    liste_display.append("patte par main droite")
                    
                elif patte2:
                    liste_display.append("patte par main gauche")

            elif bouche:
                if épaul1 or épaul2:
                    if épaul1:
                        liste_display.append("bouche par main droite")
                            
                    elif épaul2:
                        liste_display.append("bouche par main gauche")
                else:
                    liste_display.append("bouche")

                    
            elif épaul1 or épaul2:
                if épaul1:
                    liste_display.append("épaul droite")
                        
                elif épaul2:
                    liste_display.append("épaul gauche")

            elif tempe1 or tempe2:
                if tempe1:
                    liste_display.append("tempe droite")
                        
                elif tempe2:
                    liste_display.append("tempe gauche")
                    
            elif oreille1 or oreille2:
                if oreille1:
                    liste_display.append("oreille droite")
                    
                elif oreille2:
                    liste_display.append("oreille gauche")

            else:
                liste_display.append("fin")


            if liste_display[-1] == "fin":

                dico = {"milieu par main droite":1,
                        "milieu par main gauche":1,
                        "front par main droite":1,
                        "front par main gauche":1,
                        "patte droite":2,
                        "patte gauche":2,
                        "bouche par main droite":1,
                        "bouche par main gauche":1,
                        "bouche":1,
                        "épaul droite":3,
                        "épaul gauche":3,
                        "tempe droite":3,
                        "tempe gauche":3,
                        "oreille droite":4,
                        "oreille gauche":4,
                        "front":1}

                ok = 10
                val = ""
                for i in liste_display[2:]:
                    for cle, valeur in dico.items():
                        if i == cle:
                            if ok > valeur:
                                ok = valeur
                                val = cle
                
            
                liste_display = []


                
            if val != "":
                print(val)


        #epaul droite -> milieu -> epaul droite == retour 

        #-------------------------------------------------------------1

            
  

        cv2.imshow('FACE', gray)
        

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

        compteur += 1

        
    video.release()
    cv2.destroyAllWindows()


try:
    video_capture_visage()
except:
    pass





























        
