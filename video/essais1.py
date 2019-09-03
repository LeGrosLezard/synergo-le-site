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
              DIRECTION_VERTICALE, DIRECTION_HORIZONTALE):

    #On recoit si c'est un grand mouvement ou un petit
    # -> CONTOUR()

    if c > 5:

        skinMask = cv2.inRange(frame, np.array([b], dtype = "uint8"), np.array([a], dtype = "uint8"))

        if localisation is True:

            frame_detector = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]

            #Une détection apparait au niveau du visage -> mouvement du visage
            if x - 20 < x_mov and int(round(y+h*1.5)) > y_mov+h_mov:
                proba = 60
                cv2.putText(frame_movement, str("tete" + "" + str(proba) + " %"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)





            else:
                #MAINTENANT IL FAUT DETERMINER SI C LE BRAS OU LA MAIN
                counter_Wpx = 0

                #On verifie que l'interieur de la détection est une zone de peau.
                detector = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]
                
                for i in range(detector.shape[0]):
                    for j in range(detector.shape[1]):
                        if detector[i, j] == 255:
                            counter_Wpx+=1


                #On determine que c'est un mouvement du background et ou chemise.
                if counter_Wpx == 0:
                    cv2.putText(frame_movement, str("non main" + "" + "100%"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)
                


        #Une détection apparait avec une aire de plus de 1000 -> grand mouvement
        elif localisation is False:
            proba = 90

            #On détermine que c'est un mouvement de la TETE
            if x - 20 < x_mov and int(round(y+h*1.5)) > y_mov+h_mov:
                cv2.putText(frame_movement, str("TETE " + "" + str(proba) + " %"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

            
            else:
                #On determine que c'est un mouvement du BAS
                if y_mov > int(round(600*70/100)):
                
                    cv2.putText(frame_movement, str("mouvement bas " + "" + str(proba) + " %"),
                                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

                    mouvement_direction(DIRECTION_VERTICALE, y_mov, h_mov,
                                            DIRECTION_HORIZONTALE, x_mov, "bas") 
                else:
                    
                    cv2.putText(frame_movement, str("mouvement " + "" + str(proba) + " %"),
                                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)



                    mouvement_direction(DIRECTION_VERTICALE, y_mov, h_mov,
                                        DIRECTION_HORIZONTALE, x_mov, "else")



        return skinMask




def mouvement_direction(DIRECTION_VERTICALE, y, h,
                        DIRECTION_HORIZONTALE, x, zone):

    try:
        print(DIRECTION_HORIZONTALE[-1], 'x')
        print(DIRECTION_VERTICALE[-1], "y")
        print(zone)
        print("")
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














