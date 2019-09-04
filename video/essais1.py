import numpy as np
import cv2
from PIL import Image
import operator
from collections import defaultdict
import time




#ICI mouvement detecteur --------------------------------------

def original_traitement(cap, kernel_blur):

    ret, originale=cap.read()
    originale = cv2.resize(originale, (800, 600))
    originale=cv2.cvtColor(originale, cv2.COLOR_BGR2GRAY)
    originale=cv2.GaussianBlur(originale, (kernel_blur, kernel_blur), 0)
    kernel_dilate=np.ones((10, 10), np.uint8)

    return originale, kernel_dilate


def to_mask(frame, gray, originale, kernel_blur, seuil, kernel_dilate, x, y, w, h):
    
    gray=cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)

    mask=cv2.absdiff(originale, gray)
    mask[y+20:y+h-20, x+20:x+w-20] = 0
    mask=cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask=cv2.dilate(mask, kernel_dilate, iterations=5)
    contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame_contour=frame.copy()
    
    


    return contours, frame_contour




#----------------------------------------------Meme fonction
def bras_mouvement(air, frame, x, y):

    if air > 10000:
        return False
    else:
        return True


    
def contour(frame, contours, surface, frame_contour):
    
    for c in contours:
        if cv2.contourArea(c) < 100000:

            cv2.drawContours(frame_contour, [c], 0, (0, 255, 0), 5)
            if cv2.contourArea(c) < surface:
                continue

            x, y, w, h = cv2.boundingRect(c)
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            taille_area = bras_mouvement(cv2.contourArea(c), frame, x, y)

            
            return x, y, w, h, taille_area

    return None, None, None, None, False

#----------------------------------------------Meme fonction






#ICI skin detecteur--------------------------------------------------------
def face_detector(faceCascade, gray, frame):

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=1,
        minSize=(60, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)
        
        frame1 = frame[y+10:y+h-10, x+30:x+w-35]
        #cv2.imshow("dza", frame1)
        return frame1, x, y, w, h



def most_pixel(c, frame1):


    dico = {}
    img = Image.fromarray(frame1)
    for value in img.getdata():
        if value in dico.keys():
            dico[value] += 1
        else:
            dico[value] = 1
            
    sorted_x = sorted(dico.items(), key=operator.itemgetter(1), reverse=True)
    
    a = sorted_x[0][0][0] + 20, sorted_x[0][0][1] + 20, sorted_x[0][0][2] + 40
    b = sorted_x[-1][0][0], sorted_x[-1][0][1], sorted_x[-1][0][2]

    return a, b



def detector_W_px(skinMask, y_mov, h_mov, x_mov, w_mov, frame):
    counter_Wpx = 0

    #On verifie que l'interieur de la détection est une zone de peau.
    detector_skin = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]
    area_zone = frame[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]

    for i in range(detector_skin.shape[0]):
        for j in range(detector_skin.shape[1]):
            if detector_skin[i, j] == 255:
                counter_Wpx+=1
   
    return counter_Wpx



def skin_mask(frame, frame1, frame_movement, a, b, c, x, y, w, h,
              x_mov, y_mov, w_mov, h_mov, taille_area,
              DIRECTION_VERTICALE, HAND, COIN_GAUCHE, COIN_DROIT):


    ok_detection = False


    
    if c > 5:
        skinMask = cv2.inRange(frame, np.array([b], dtype = "uint8"), np.array([a], dtype = "uint8"))
        
        #PETIT MOUVEMENT
        if taille_area is True:

            frame_detector = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]

            #VISAGE
            if x + 20 < x_mov and y+h-20 > y_mov+h_mov and x+w-20 > x_mov+w_mov and y + 20 > y_mov:
                hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, "main", skinMask, COIN_DROIT, COIN_GAUCHE)

                
                
            #AUTRE
            else:


                counter_Wpx = detector_W_px(skinMask, y_mov, h_mov, x_mov, w_mov, frame)
                #NON MAIN
                if counter_Wpx == 0:
                    cv2.putText(frame_movement, str("non main"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)
           
    
                #MAIN
                elif counter_Wpx > 0:

                    #BAS
                    if y_mov+h_mov > int(round(600*80/100)):

                        if DIRECTION_VERTICALE[-1] - x_mov < 250:
                            #droite
                            if x_mov < x+w/2:
                                hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, "bas gauche", skinMask, COIN_DROIT, COIN_GAUCHE)
                            #gauche
                            elif x_mov > x+w/2:
                                hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, "bas droite", skinMask, COIN_DROIT, COIN_GAUCHE)

                                
                                

                    #MILIEU
                    elif y_mov+h_mov > int(round(600*50/100)) and y_mov+h_mov < int(round(600*80/100)):

                        if DIRECTION_VERTICALE[-1] - x_mov < 250:
        
                            #droite
                            if x_mov < x+w/2:
                                hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, "milieu gauche", skinMask, COIN_DROIT, COIN_GAUCHE)
                            #gauche
                            elif x_mov > x+w/2:
                                hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, "milieu droite", skinMask, COIN_DROIT, COIN_GAUCHE)
                         


                    #HAUT
                    elif y_mov+h_mov < int(round(600*50/100)):

    
                        if DIRECTION_VERTICALE[-1] - x_mov < 250:

                            
                            #droite
                            if x_mov < x+w/2:
                                hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, "haut gauche", skinMask, COIN_DROIT, COIN_GAUCHE)
                            #gauche
                            elif x_mov > x+w/2:
                                hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, "haut droite", skinMask, COIN_DROIT, COIN_GAUCHE)

                            




        #GRAND MOUVEMENT
        elif taille_area is False:

            #ZONE TETE
            if x - 30 < x_mov and int(round(y+h+45)) > y_mov+h_mov:
                pass

            #AUTRE ZONE
            else:
            
                #BAS
                if y_mov+h_mov > int(round(600*80/100)):
                    #droite
                    if x_mov < x+w/2:
                        m = mouvement_direction(frame_movement, skinMask, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, w_mov, "bas gauche", COIN_DROIT, COIN_GAUCHE)
                    #gauche
                    elif x_mov > x+w/2:

                        m = mouvement_direction(frame_movement, skinMask, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, w_mov, "bas droite", COIN_DROIT, COIN_GAUCHE)
                    

                    
                #MILLIEU
                elif y_mov+h_mov > int(round(600*50/100)) and y_mov+h_mov < int(round(600*80/100)):
                    #droite
                    if x_mov < x+w/2:
                        m = mouvement_direction(frame_movement, skinMask, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, w_mov, "milieu gauche", COIN_DROIT, COIN_GAUCHE)
                    #gauche
                    elif x_mov > x+w/2:
                        m = mouvement_direction(frame_movement, skinMask, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, w_mov, "milieu droite", COIN_DROIT, COIN_GAUCHE)
                 
                




                #HAUT
                elif y_mov+h_mov <= int(round(600*50/100)):
                    #droite
                    if x_mov < x+w/2:
                        m = mouvement_direction(frame_movement, skinMask, DIRECTION_VERTICALE, y_mov, h_mov,
                                                DIRECTION_HORIZONTALE, x_mov, w_mov, "haut gauche", COIN_DROIT, COIN_GAUCHE)
                    #gauche
                    elif x_mov > x+w/2:
                        m = mouvement_direction(frame_movement, skinMask, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, w_mov, "haut droite", COIN_DROIT, COIN_GAUCHE)
            









        return skinMask, m, y_mov, h_mov, x_mov, w_mov






def hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, w_mov, zone, skinMask, COIN_DROIT, COIN_GAUCHE):
    

    crop = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]
    c = 0
    for i in range(crop.shape[0]):
        for j in range(crop.shape[1]):
            if crop[i, j] == 255:
                c += 1
    
    if c > 0:
        print(COIN_GAUCHE[-1], COIN_DROIT[-1], x_mov, y_mov+h_mov)
        cv2.rectangle(frame_movement, (x_mov, y_mov), (x_mov+w_mov, y_mov+h_mov), (0, 0, 255), 2)
        cv2.putText(frame_movement, str("main"),
                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)






def mouvement_direction(frame_movement, skinMask, DIRECTION_VERTICALE, y, h, x, w, zone, COIN_DROIT, COIN_GAUCHE):


    cv2.rectangle(frame_movement, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(frame_movement, str("mouvement" + " " + str(zone)),
                (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

    COIN_GAUCHE.append(x)
    COIN_DROIT.append(y+h)
    DIRECTION_VERTICALE.append(y+h)
    return ""




#----------------------------------------------------------------------MEME FONCTION 1

def initialisation_zone(liste, y, h, x, w):

    liste[0].append(y)
    liste[1].append(h)
    liste[2].append(x)
    liste[3].append(w)



def init_zones(x, y, w, h, frame_area,
               ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9,
               ll10, ll11, ll12, ll13, ll14, ll15):



    initialisation_zone(ll1, y, y + h + 10, x - w - 30, x - 60)
    #droite

    initialisation_zone(ll2, y, y + h + 10, x + w + 60, x + w * 2 + 30)
    #gauche


    initialisation_zone(ll3, y - int(round(150 * 100 / h)), y - int(round(80 * 100 / h)),
                        x + int(round(w/3)), x + int(round(w/3)) * 2)
    #milieu


    initialisation_zone(ll4, y - int(round(110 * 100 / h)), y - int(round(50 * 100 / h)),
                        x - 20, x + 30)
    #patte droite

    initialisation_zone(ll5, y - int(round(110 * 100 / h)), y - int(round(50 * 100 / h)),
                        x + w - 20, x + w + 30)
    
    #patte gauche



    initialisation_zone(ll6, y + h - 50, y + h, x + int(round(w/3)), x + int(round(w/3)) * 2)
    #bouche

    initialisation_zone(ll7, y + h + 10, y + h + 45, x + int(round(w/3)), x + int(round(w/3)) * 2)
    #menton


    initialisation_zone(ll8, y + h + 120,y + h + 180, x, x + w)
    #buste 


    initialisation_zone(ll9, y + h + 20, y + h + 60, x - 50, x + 30)
    #épaul droite


    initialisation_zone(ll10, y + h + 20, y + h + 60, x + w - 30, x + w + 30)
    #épaul gauche


    initialisation_zone(ll11, y - int(round(30 * 100 / h)),
                        y - int(round(-40 * 100 / h)), x + 30, x + w - 30)
    #front

    initialisation_zone(ll12, y - 20,y + 40, x - 40, x)
    #tempe droite

    initialisation_zone(ll13, y - 20, y + 40, x + w, x + w + 40)
    #tempe gauche

    initialisation_zone(ll14, y + 70, y + 110, x - 40, x)
    #oreille droite


    initialisation_zone(ll15, y + 70, y + 110, x + w, x + w + 40)
    #oreille gauche





def zones_area_build(liste, gray):
    
    y1 = round(int(sum(liste[0]) / len(liste[0])))
    yh1 = round(int(sum(liste[1]) / len(liste[1])))
    x1 = round(int(sum(liste[2]) / len(liste[2])))
    xw1 = round(int(sum(liste[3]) / len(liste[3])))

    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop = gray[y1:yh1, x1:xw1]

    return crop


#----------------------------------------------------------------------MEME FONCTION 1




#----------------------------------------------------------------------MEME FONCTION 2
def into_crop(crop):
    for i in range(crop.shape[0]):
        for j in range(crop.shape[1]):
            if crop[i, j][0] ==  0 and\
               crop[i, j][1] == 0 and\
               crop[i, j][2] == 255:
                return True
    return None


def detection_movement(crop1, crop2, crop3, crop4,
                       crop5, crop6, crop7, crop8,
                       crop9, crop10, crop11, crop12,
                       crop13, crop14, crop15, oki_detection):

    droite = into_crop(crop2)
    milieu = into_crop(crop1)
    gauche = into_crop(crop3)
    patte_droite = into_crop(crop4)
    patte_gauche = into_crop(crop5)
    bouche = into_crop(crop6)
    menton = into_crop(crop7)
    buste = into_crop(crop8)
    epaul_droite = into_crop(crop9)
    epaul_gauchee = into_crop(crop10)
    front = into_crop(crop11)
    tempe_droite = into_crop(crop12)
    tempe_gauche = into_crop(crop13)
    oreille_droite = into_crop(crop14)
    oreille_gauche = into_crop(crop15)

    dico = {"droite":droite, "milieu":milieu, "gauche":gauche,
            "patte_droite":patte_droite, "bouche":bouche,
            "patte_gauche":patte_gauche, "menton":menton,
            "buste":buste, "epaul_droite":epaul_droite,
            "epaul_gauchee":epaul_gauchee, "front":front,
            "tempe_droite":tempe_droite, "tempe_gauche":tempe_gauche,
             "oreille_droite":oreille_droite, "oreille_gauche":oreille_gauche}

    if oki_detection is True:
        for cle, valeur in dico.items():
            if valeur is True:
                print(cle, valeur)


    

def zones_area(gray, ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9,
               ll10, ll11, ll12, ll13, ll14, ll15, oki_detection):
    

    crop1 = zones_area_build(ll1, gray)

    crop2 = zones_area_build(ll2, gray)

    crop3 = zones_area_build(ll3, gray)

    crop4 = zones_area_build(ll4, gray)

    crop5 = zones_area_build(ll5, gray)

    crop6 = zones_area_build(ll6, gray)

    crop7 = zones_area_build(ll7, gray)

    crop8 = zones_area_build(ll8, gray)

    crop9 = zones_area_build(ll9, gray)

    crop10 = zones_area_build(ll10, gray)

    crop11 = zones_area_build(ll11, gray)

    crop12 = zones_area_build(ll12, gray)

    crop13 = zones_area_build(ll13, gray)

    crop14 = zones_area_build(ll14, gray)
  
    crop15 = zones_area_build(ll15, gray)

    

    detection_movement(crop1, crop2, crop3, crop4,
                        crop5, crop6, crop7, crop8,
                        crop9, crop10, crop11, crop12,
                        crop13, crop14, crop15, oki_detection)


        


#----------------------------------------------------------------------MEME FONCTION 2
























