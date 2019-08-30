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

SUBSTRACTOR15 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)
SUBSTRACTOR16 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)
SUBSTRACTOR17 = cv2.createBackgroundSubtractorMOG2(history=100,
                                                varThreshold=50,
                                                detectShadows=True)

def video_capture_visage():

    #k, j, l, m <- video jb

    #for displaying video
    video = cv2.VideoCapture("j.mp4")
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
    


    MOUVEMENT = [0]
    
    listee = []


    liste_display = []
    compteur = 0
    compteur1 = 0


    #----------------------------------------------------
    """
    Il faut init
    Il faut coté droit sinon non poru se toucher la tete




    """
    #----------------------------------------------------




    
    activate_compteur = False
    active_compteur = 0
    ok = 0
    stop = False
    while(True):



        ret, frame_visage = video.read()
        frame_visage = cv2.resize(frame_visage, (1000, 800))
    
        gray = cv2.cvtColor(frame_visage, cv2.COLOR_BGR2GRAY)
        the_mask = SUBSTRACTOR1.apply(gray)
        
        
        
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=3,
            minNeighbors=1, minSize=(60, 100),
            flags=cv2.CASCADE_SCALE_IMAGE)


        for x, y, w, h in faces:
            

            if MOUVEMENT[-1] > x + 5 or MOUVEMENT[-1] < x - 5:
                stop = True

                if ok >= 2:
                    
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

                    stop = False


                
            MOUVEMENT.append(x)
            



            
            #cv2.rectangle(gray, (x,y), (x+w, y+h),(255), 2)




            
            def detection(mask, l, phrase, nb, x):
                """Here we ask the sum of the list(we insert element in list
                from the box). if the mean > + 50000 there is movement in there"""
                try:
                    #doing the sum of elements of the list
                    liste = sum([j for i in mask for j in i])
                    #we add the sum of all element
                    l.append(liste)
                    #if the current list of detection is > at the mean of all passation
                    #a refaire
                    if liste > sum(l)/len(l) + nb:
                        #we return the point detected
                        return phrase
                except:
                    pass




            if len(ll3[0]) < 2:
                
                activate_compteur = True
                ll3[0].append(y)
                ll3[1].append(y + h + 10)
                ll3[2].append(x - w - 30)
                ll3[3].append(x - 60)
                #droite


                ll4[0].append(y)
                ll4[1].append(y + h + 10)
                ll4[2].append(x + w + 80)
                ll4[3].append(x + w * 2 + 30)
                #gauche


                ll5[0].append(y - int(round(150 * 100 / h)))
                ll5[1].append(y - int(round(80 * 100 / h)))
                ll5[2].append(x + int(round(w/3)))
                ll5[3].append(x + int(round(w/3)) * 2)
                #milieu



                ll6[0].append(y - int(round(110 * 100 / h)))
                ll6[1].append(y - int(round(50 * 100 / h)))
                ll6[2].append( x - 20)
                ll6[3].append(x + 30)
                #patte droite


                ll7[0].append(y - int(round(110 * 100 / h)))
                ll7[1].append(y - int(round(50 * 100 / h)))
                ll7[2].append(x + w - 20)
                ll7[3].append(x + w + 30)
                #patte gauche


                ll8[0].append(y + h - 50)
                ll8[1].append(y + h)
                ll8[2].append(x + int(round(w/3)))
                ll8[3].append(x + int(round(w/3)) * 2)
                #bouche


                ll9[0].append(y + h + 10)
                ll9[1].append(y + h + 45)
                ll9[2].append(x + int(round(w/3)))
                ll9[3].append(x + int(round(w/3)) * 2)
                #menton

                ll10[0].append(y + h + 120)
                ll10[1].append(y + h + 180)
                ll10[2].append(x)
                ll10[3].append(x + w)
                #buste 

                ll11[0].append(y + h + 20)
                ll11[1].append(y + h + 60)
                ll11[2].append(x - 50)
                ll11[3].append(x + 30)
                #épaul droite



                ll12[0].append(y + h + 20)
                ll12[1].append(y + h + 60)
                ll12[2].append(x + w - 30)
                ll12[3].append(x + w + 50)
                #épaul gauche

                ll13[0].append(y - int(round(30 * 100 / h)))
                ll13[1].append(y - int(round(-40 * 100 / h)))
                ll13[2].append(x + 30)
                ll13[3].append(x + w - 30)
                #front

      
                ll14[0].append(y - 20)
                ll14[1].append(y + 40)
                ll14[2].append(x - 40)
                ll14[3].append(x)
                #tempe droite


                ll15[0].append(y - 20)
                ll15[1].append(y + 40)
                ll15[2].append(x + w)
                ll15[3].append(x + w + 40)
                #tempe gauche


                ll16[0].append(y + 70)
                ll16[1].append(y + 130)
                ll16[2].append(x - 40)
                ll16[3].append(x)
                #oreille droite

                ll17[0].append(y + 70)
                ll17[1].append(y + 130)
                ll17[2].append(x + w)
                ll17[3].append(x + w + 40)
                #oreille gauche

        
        if len(ll3[0]) >= 2:
            if active_compteur > 2:
                active_compteur = False
            
            y1 = round(int(sum(ll3[0]) / len(ll3[0])))
            yh1 = round(int(sum(ll3[1]) / len(ll3[1])))
            x1 = round(int(sum(ll3[2]) / len(ll3[2])))
            xw1 = round(int(sum(ll3[3]) / len(ll3[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop3 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop3 for j in i])
            try:
                if liste > sum(l)/len(l) + 100000 and active_compteur is False:
                    #print("droite")
                    liste_display.append("droite")
                    
            except:
                pass
            l.append(liste)



            y1 = round(int(sum(ll4[0]) / len(ll4[0])))
            yh1 = round(int(sum(ll4[1]) / len(ll4[1])))
            x1 = round(int(sum(ll4[2]) / len(ll4[2])))
            xw1 = round(int(sum(ll4[3]) / len(ll4[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop4 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop4 for j in i])
            try:
                if liste > sum(l1)/len(l1) + 100000 and active_compteur is False:
                    #print("gauche")
                    liste_display.append("gauche")
                    
            except:
                pass
            l1.append(liste)

            y1 = round(int(sum(ll5[0]) / len(ll5[0])))
            yh1 = round(int(sum(ll5[1]) / len(ll5[1])))
            x1 = round(int(sum(ll5[2]) / len(ll5[2])))
            xw1 = round(int(sum(ll5[3]) / len(ll5[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop5 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop5 for j in i])
            try:
                if liste > sum(l2)/len(l2) + 100000 and active_compteur is False:
                    #print("milieu")
                    liste_display.append("milieu")
                    
            except:
                pass
            l2.append(liste)
 


            y1 = round(int(sum(ll6[0]) / len(ll6[0])))
            yh1 = round(int(sum(ll6[1]) / len(ll6[1])))
            x1 = round(int(sum(ll6[2]) / len(ll6[2])))
            xw1 = round(int(sum(ll6[3]) / len(ll6[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop6 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop6 for j in i])
            try:
                if liste > sum(l3)/len(l3) + 100000 and active_compteur is False:
                    #print("patte droite")
                    liste_display.append("patte droite")
                    
            except:
                pass
            l3.append(liste)
       
                

            y1 = round(int(sum(ll7[0]) / len(ll7[0])))
            yh1 = round(int(sum(ll7[1]) / len(ll7[1])))
            x1 = round(int(sum(ll7[2]) / len(ll7[2])))
            xw1 = round(int(sum(ll7[3]) / len(ll7[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop7 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop7 for j in i])
            try:
                if liste > sum(l4)/len(l4) + 100000 and active_compteur is False:
                    #print("patte gauche")
                    liste_display.append("patte gauche")
                    
            except:
                pass
            l4.append(liste)
            

            y1 = round(int(sum(ll8[0]) / len(ll8[0])))
            yh1 = round(int(sum(ll8[1]) / len(ll8[1])))
            x1 = round(int(sum(ll8[2]) / len(ll8[2])))
            xw1 = round(int(sum(ll8[3]) / len(ll8[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop8 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop8 for j in i])
            try:
                if liste > sum(l5)/len(l5) + 100000 and active_compteur is False:
                    #print("bouche")
                    liste_display.append("bouche")
                    
            except:
                pass
            l5.append(liste)

            y1 = round(int(sum(ll9[0]) / len(ll9[0])))
            yh1 = round(int(sum(ll9[1]) / len(ll9[1])))
            x1 = round(int(sum(ll9[2]) / len(ll9[2])))
            xw1 = round(int(sum(ll9[3]) / len(ll9[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop9 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop9 for j in i])
            try:
                if liste > sum(l6)/len(l6) + 10000 and active_compteur is False:
                    #print("menton")
                    liste_display.append("menton")
                    
            except:
                pass
            l6.append(liste)



            y1 = round(int(sum(ll10[0]) / len(ll10[0])))
            yh1 = round(int(sum(ll10[1]) / len(ll10[1])))
            x1 = round(int(sum(ll10[2]) / len(ll10[2])))
            xw1 = round(int(sum(ll10[3]) / len(ll10[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop10 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop10 for j in i])
            try:
                if liste > sum(l7)/len(l7) + 200000 and active_compteur is False:
                    #print("buste")
                    liste_display.append("buste")
                    
            except:
                pass
            l7.append(liste)
                

            y1 = round(int(sum(ll11[0]) / len(ll11[0])))
            yh1 = round(int(sum(ll11[1]) / len(ll11[1])))
            x1 = round(int(sum(ll11[2]) / len(ll11[2])))
            xw1 = round(int(sum(ll11[3]) / len(ll11[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop11 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop11 for j in i])
            try:
                if liste > sum(l8)/len(l8) + 80000 and active_compteur is False:
                    #print("épaule droite")
                    liste_display.append("épaule droite")
            except:
                pass
            l8.append(liste)
                

            y1 = round(int(sum(ll12[0]) / len(ll12[0])))
            yh1 = round(int(sum(ll12[1]) / len(ll12[1])))
            x1 = round(int(sum(ll12[2]) / len(ll12[2])))
            xw1 = round(int(sum(ll12[3]) / len(ll12[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop12 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop12 for j in i])
            try:
                if liste > sum(l9)/len(l9) + 80000 and active_compteur is False:
                    #print("épaule gauche")
                    liste_display.append("épaule gauche")
                    
            except:
                pass
            l9.append(liste)
                

            y1 = round(int(sum(ll13[0]) / len(ll13[0])))
            yh1 = round(int(sum(ll13[1]) / len(ll13[1])))
            x1 = round(int(sum(ll13[2]) / len(ll13[2])))
            xw1 = round(int(sum(ll13[3]) / len(ll13[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop13 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop13 for j in i])
            try:
                if liste > sum(l10)/len(l10) + 100000 and active_compteur is False:
                    #print("front")
                    liste_display.append("front")
                    
            except:
                pass
            l10.append(liste)
                
            
            y1 = round(int(sum(ll14[0]) / len(ll14[0])))
            yh1 = round(int(sum(ll14[1]) / len(ll14[1])))
            x1 = round(int(sum(ll14[2]) / len(ll14[2])))
            xw1 = round(int(sum(ll14[3]) / len(ll14[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop14 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop14 for j in i])
            try:
                if liste > sum(l11)/len(l11) + 100000 and active_compteur is False:
                    #print("tempe droite")
                    liste_display.append("tempe droite")
                    
            except:
                pass
            l11.append(liste)
                


            y1 = round(int(sum(ll15[0]) / len(ll15[0])))
            yh1 = round(int(sum(ll15[1]) / len(ll15[1])))
            x1 = round(int(sum(ll15[2]) / len(ll15[2])))
            xw1 = round(int(sum(ll15[3]) / len(ll15[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop15 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop15 for j in i])
            try:
                if liste > sum(l12)/len(l12) + 100000 and active_compteur is False:
                    #print("tempe gauche")
                    liste_display.append("tempe gauche")
                    
            except:
                pass
            l12.append(liste)


                
            y1 = round(int(sum(ll16[0]) / len(ll16[0])))
            yh1 = round(int(sum(ll16[1]) / len(ll16[1])))
            x1 = round(int(sum(ll16[2]) / len(ll16[2])))
            xw1 = round(int(sum(ll16[3]) / len(ll16[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop16 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop16 for j in i])
            
            try:
                #print(liste, sum(l13)/len(l13))
                if liste > sum(l13)/len(l13) + 10000 and active_compteur is False:
                    #print("oreille droite")
                    liste_display.append("oreille droite")
                    
            except:
                pass
            l13.append(liste)
                

            y1 = round(int(sum(ll17[0]) / len(ll17[0])))
            yh1 = round(int(sum(ll17[1]) / len(ll17[1])))
            x1 = round(int(sum(ll17[2]) / len(ll17[2])))
            xw1 = round(int(sum(ll17[3]) / len(ll17[3])))
            
            cv2.rectangle(the_mask, (x1, y1), (xw1, yh1), (255), 3)
            crop17 = the_mask[y1:yh1, x1:xw1]
            liste = sum([j for i in crop17 for j in i])
            try:
                if liste > sum(l14)/len(l14) + 10000 and active_compteur is False:
                    #print("oreille gauche")
                    liste_display.append("oreille gauche")
                    
            except:
                pass
            l14.append(liste)


                
        if activate_compteur is True:
            active_compteur += 1
            

            for i in liste_display:

                if i in ("buste"):
                    dico = {"milieu":1,
                            "bouche":1,
                            "menton":2,
                            "épaule droite":1,
                            "épaule gauche":1,
                            "buste":4}
                    val = 10
                    donc = ""
                    for i in liste_display:
                        for cle, valeur in dico.items():
                            if i == cle and val > valeur:
                                val = valeur
                                donc = cle
                    if donc != "":
                        print(donc)
                        
                    liste_display = []



                
                elif i in ("droite", "gauche"):
       
                    val = 10
                    donc = ""
                    dico = {"milieu":1,
                            "patte droite":2,
                            "patte gauche":2,
                            "bouche":1,
                            "épaule droite":3,
                            "épaule gauche":3,
                            "tempe droite":3,
                            "tempe gauche":3,
                            "oreille droite":4,
                            "oreille gauche":4,
                            "front":1,
                            "droite":5,
                            "gauche":5}
                    

                    else:
                        for i in liste_display:
                            for cle, valeur in dico.items():
                                if i == cle and val > valeur:
                                    val = valeur
                                    donc = cle

                        if donc != "":
                            print(donc)
                        
                    liste_display = []
                else:
                    pass




                



        cv2.imshow("dzadaz", the_mask)
        #cv2.imshow('FACE', gray)


        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


        compteur += 1
        if stop is True:
            ok += 1

        
    video.release()
    cv2.destroyAllWindows()



video_capture_visage()






























        
