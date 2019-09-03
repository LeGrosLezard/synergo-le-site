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


def to_mask(frame, gray, originale, kernel_blur, seuil, kernel_dilate):
    
    gray=cv2.GaussianBlur(gray, (kernel_blur, kernel_blur), 0)
    mask=cv2.absdiff(originale, gray)
    mask=cv2.threshold(mask, seuil, 255, cv2.THRESH_BINARY)[1]
    mask=cv2.dilate(mask, kernel_dilate, iterations=5)
    contours, nada=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame_contour=frame.copy()

    return contours, frame_contour




#----------------------------------------------Meme fonction
def bras_mouvement(air, frame, x, y):
    proba = 100

    if air > 9500:
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
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            localisation = bras_mouvement(cv2.contourArea(c), frame, x, y)

            
            return x, y, w, h, localisation

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




 
def skin_mask(frame, frame1, frame_movement, a, b, c, x, y, w, h,
              x_mov, y_mov, w_mov, h_mov, localisation,
              DIRECTION_VERTICALE, DIRECTION_HORIZONTALE, HAND):

    #On recoit si c'est un grand mouvement ou un petit
    # -> CONTOUR()

    if c > 5:

        skinMask = cv2.inRange(frame, np.array([b], dtype = "uint8"), np.array([a], dtype = "uint8"))

        #PETIT MOUVEMENT
        if localisation is True:

            frame_detector = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]

            #VISAGE
            if x - 20 < x_mov and int(round(y+h*1.5)) > y_mov+h_mov:
                proba = 60
                cv2.putText(frame_movement, str("tete" + "" + str(proba) + " %"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

                #hand_movement(HAND, y_mov, h_mov, "tete")
            

            else:
                counter_Wpx = 0


                print(x+w, y+h)


                

                #On verifie que l'interieur de la détection est une zone de peau.
                detector_skin = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]
                area_zone = frame[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]

                for i in range(detector_skin.shape[0]):
                    for j in range(detector_skin.shape[1]):
                        if detector_skin[i, j] == 255:
                            counter_Wpx+=1
    
                
                #NON MAIN
                if counter_Wpx == 0:
                    cv2.putText(frame_movement, str("non main" + "" + "100%"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

                #MAIN ?
                elif counter_Wpx > 0:
                    #BAS
                    if y_mov+h_mov > int(round(600*80/100)):
                        hand_movement(HAND, y_mov, h_mov, "bas")
                        cv2.putText(frame_movement, str("bas" + "" + "100%"),
                                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)
  
                    #MILIEU
                    elif y_mov+h_mov > int(round(600*50/100)) and y_mov+h_mov < int(round(600*80/100)):
                        hand_movement(HAND, y_mov, h_mov, "milieu")
                        cv2.putText(frame_movement, str("milieu" + "" + "100%"),
                                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)


                        
                    #HAUT
                    elif y_mov+h_mov < int(round(600*50/100)):
                        hand_movement(HAND, y_mov, h_mov, "haut")
                        cv2.putText(frame_movement, str("haut" + "" + "100%"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)











        #GRAND MOUVEMENT
        elif localisation is False:
            proba = 90


            #ZONE TETE
            if x - 20 < x_mov and int(round(y+h*2)) > y_mov+h_mov:
                cv2.putText(frame_movement, str("TETE " + "" + str(proba) + " %"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

                mouvement_direction(DIRECTION_VERTICALE, y_mov, h_mov,
                                    DIRECTION_HORIZONTALE, x_mov, "tete")

            #AUTRE ZONE
            else:
            
                #BAS
                if y_mov+h_mov > int(round(600*80/100)):
                    
                    cv2.putText(frame_movement, str("mouvement bas " + "" + str(proba) + " %"),
                                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

                    mouvement_direction(DIRECTION_VERTICALE, y_mov, h_mov,
                                            DIRECTION_HORIZONTALE, x_mov, "bas")


                #MILLIEU
                elif y_mov+h_mov > int(round(600*50/100)) and y_mov+h_mov < int(round(600*80/100)):
                    
                    cv2.putText(frame_movement, str("mouvement milieu" + "" + str(proba) + " %"),
                                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

                    mouvement_direction(DIRECTION_VERTICALE, y_mov, h_mov,
                                        DIRECTION_HORIZONTALE, x_mov, "milieu")
                    

                #HAUT
                elif y_mov+h_mov < int(round(600*50/100)):

                    cv2.putText(frame_movement, str("mouvement haut" + "" + str(proba) + " %"),
                                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

                    mouvement_direction(DIRECTION_VERTICALE, y_mov, h_mov,
                                        DIRECTION_HORIZONTALE, x_mov, "haut")



        return skinMask


#LE BUT C DE DIRE GRAND MOUVEMENT ALORS TROUVE MAIN DONC GRAND ACTIVE PETIT


def hand_movement(HAND, y_mov, h_mov, zone):
    
    try:
        #print(HAND[-1], zone)
        print("main", zone)
    except:
        pass

    HAND.append(y_mov+h_mov)




def mouvement_direction(DIRECTION_VERTICALE, y, h,
                        DIRECTION_HORIZONTALE, x, zone):


    try:
        #print('x', DIRECTION_HORIZONTALE[-1], x)
        #print('y+h', DIRECTION_VERTICALE[-1], y+h)
        print("mouvement", zone)
        #print("")
    except:
        pass
    
    DIRECTION_VERTICALE.append(y+h)
    DIRECTION_HORIZONTALE.append(x)


    #LE BUT EST DE SUIVRE LA MAIN







    #IDEE IA
    #Le but serait de lui dire -> RETIENT TOUS LES CADRES FREDO
    #si un cadre pop maintenant dans les + ou - 20 px
    #ALORS c la main
    #en arretant toutes les conditions passées.

    #CONDITION la vidéo doit durée + de 20 minutes et pas de plan coupé.
    #Ne marche qu'avec le bas et pas la tete





#--------------------------------------------------FIGURE DETECTION

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














