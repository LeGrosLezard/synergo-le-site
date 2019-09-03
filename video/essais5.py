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
              DIRECTION_VERTICALE, HAND,
              hand_detection):

    #On recoit si c'est un grand mouvement ou un petit
    # -> CONTOUR()

    if c > 5:

        skinMask = cv2.inRange(frame, np.array([b], dtype = "uint8"), np.array([a], dtype = "uint8"))
        
        #PETIT MOUVEMENT
        if taille_area is True:

            frame_detector = skinMask[y_mov:y_mov+h_mov, x_mov:x_mov+w_mov]

            #VISAGE
            if x - 20 < x_mov and int(round(y+h*1.5)) > y_mov+h_mov:
                if hand_detection is True:
                    hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, "tete")
                    print(DIRECTION_VERTICALE[-1], x_mov)
                m = False


            #AUTRE
            else:

                counter_Wpx = detector_W_px(skinMask, y_mov, h_mov, x_mov, w_mov, frame)

                #NON MAIN
                if counter_Wpx == 0:
                    cv2.putText(frame_movement, str("non main"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)
                    m = False
    

                #MAIN
                elif counter_Wpx > 0:

                    #BAS
                    if y_mov+h_mov > int(round(600*80/100)):
                        if hand_detection is True:
                            m = False
                            if DIRECTION_VERTICALE[-1] - x_mov < 250:
                                print(DIRECTION_VERTICALE[-1], x_mov)
                                #droite
                                if x_mov < x+w/2:
                                    hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, "bas gauche")
                                #gauche
                                elif x_mov > x+w/2:
                                    hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, "bas droite")


                    #MILIEU
                    elif y_mov+h_mov > int(round(600*50/100)) and y_mov+h_mov < int(round(600*80/100)):
                        if hand_detection is True:
                            m = False
                            if DIRECTION_VERTICALE[-1] - x_mov < 250:
                                print(DIRECTION_VERTICALE[-1], x_mov)
                                #droite
                                if x_mov < x+w/2:
                                    hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, "milieu gauche")
                                #gauche
                                elif x_mov > x+w/2:
                                    hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, "milieu droite")



                    #HAUT
                    elif y_mov+h_mov < int(round(600*50/100)):
                        if hand_detection is True:
                            m = False
                            if DIRECTION_VERTICALE[-1] - x_mov < 250:
                                print(DIRECTION_VERTICALE[-1], x_mov)
                                #droite
                                if x_mov < x+w/2:
                                    hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, "haut gauche")
                                #gauche
                                elif x_mov > x+w/2:
                                    hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, "haut droite")

                                




        #GRAND MOUVEMENT
        elif taille_area is False:

            #ZONE TETE
            if x - 30 < x_mov and int(round(y+h+45)) > y_mov+h_mov:
                cv2.putText(frame_movement, str("TETE"),
                            (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)


            #AUTRE ZONE
            else:
            
                #BAS
                if y_mov+h_mov > int(round(600*80/100)):
                    #droite
                    if x_mov < x+w/2:
                        m = mouvement_direction(frame_movement, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, "bas gauche")
                    #gauche
                    elif x_mov > x+w/2:

                        m = mouvement_direction(frame_movement,DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, "bas droite")



                #MILLIEU
                elif y_mov+h_mov > int(round(600*50/100)) and y_mov+h_mov < int(round(600*80/100)):
                    #droite
                    if x_mov < x+w/2:
                        m = mouvement_direction(frame_movement, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, "milieu gauche")
                    #gauche
                    elif x_mov > x+w/2:
                        m = mouvement_direction(frame_movement, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, "milieu droite")




                #HAUT
                elif y_mov+h_mov <= int(round(600*50/100)):
                    #droite
                    if x_mov < x+w/2:
                        m = mouvement_direction(frame_movement, DIRECTION_VERTICALE, y_mov, h_mov,
                                                DIRECTION_HORIZONTALE, x_mov, "haut gauche")
                    #gauche
                    elif x_mov > x+w/2:
                        m = mouvement_direction(frame_movement, DIRECTION_VERTICALE, y_mov, h_mov,
                                                x_mov, "haut droite")


   
        return skinMask, m





def hand_movement(frame_movement, HAND, x_mov, y_mov, h_mov, zone):
    
    try:
        #print(HAND[-1], zone)
        print("main", zone)
    except:
        pass

    cv2.putText(frame_movement, str("main " + " " + str(zone)),
                (x_mov, y_mov), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)

    HAND.append(y_mov+h_mov)




def mouvement_direction(frame_movement, DIRECTION_VERTICALE, y, h, x, zone):


    try:
        print("mouvement", zone)
    except:
        pass


    cv2.putText(frame_movement, str("mouvement" + " " + str(zone)),
                (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255),1,cv2.LINE_AA)


    DIRECTION_VERTICALE.append(y+h)



    return True

    

def init_zones(x, y, w, h, frame_area,
               ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9, ll10, ll11, ll12, ll13, ll14, ll15):


    ll1[0].append(y)
    ll1[1].append(y + h + 10)
    ll1[2].append(x - w - 30)
    ll1[3].append(x - 60)
    #droite

    ll2[0].append(y)
    ll2[1].append(y + h + 10)
    ll2[2].append(x + w + 60)
    ll2[3].append(x + w * 2 + 30)
    #milieu


    ll3[0].append(y - int(round(150 * 100 / h)))
    ll3[1].append(y - int(round(80 * 100 / h)))
    ll3[2].append(x + int(round(w/3)))
    ll3[3].append(x + int(round(w/3)) * 2)
    #gauche



    ll4[0].append(y - int(round(110 * 100 / h)))
    ll4[1].append(y - int(round(50 * 100 / h)))
    ll4[2].append( x - 20)
    ll4[3].append(x + 30)
    #patte droite


    ll5[0].append(y - int(round(110 * 100 / h)))
    ll5[1].append(y - int(round(50 * 100 / h)))
    ll5[2].append(x + w - 20)
    ll5[3].append(x + w + 30)
    #patte gauche


    ll6[0].append(y + h - 50)
    ll6[1].append(y + h)
    ll6[2].append(x + int(round(w/3)))
    ll6[3].append(x + int(round(w/3)) * 2)
    #bouche


    ll7[0].append(y + h + 10)
    ll7[1].append(y + h + 45)
    ll7[2].append(x + int(round(w/3)))
    ll7[3].append(x + int(round(w/3)) * 2)
    #menton

    ll8[0].append(y + h + 120)
    ll8[1].append(y + h + 180)
    ll8[2].append(x)
    ll8[3].append(x + w)
    #buste 

    ll9[0].append(y + h + 20)
    ll9[1].append(y + h + 60)
    ll9[2].append(x - 50)
    ll9[3].append(x + 30)
    #épaul droite



    ll10[0].append(y + h + 20)
    ll10[1].append(y + h + 60)
    ll10[2].append(x + w - 30)
    ll10[3].append(x + w + 30)
    #épaul gauche

    ll11[0].append(y - int(round(30 * 100 / h)))
    ll11[1].append(y - int(round(-40 * 100 / h)))
    ll11[2].append(x + 30)
    ll11[3].append(x + w - 30)
    #front


    ll12[0].append(y - 20)
    ll12[1].append(y + 40)
    ll12[2].append(x - 40)
    ll12[3].append(x)
    #tempe droite


    ll13[0].append(y - 20)
    ll13[1].append(y + 40)
    ll13[2].append(x + w)
    ll13[3].append(x + w + 40)
    #tempe gauche


    ll14[0].append(y + 70)
    ll14[1].append(y + 110)
    ll14[2].append(x - 40)
    ll14[3].append(x)
    #oreille droite

    ll15[0].append(y + 70)
    ll15[1].append(y + 110)
    ll15[2].append(x + w)
    ll15[3].append(x + w + 40)
    #oreille gauche







def zones(gray, ll1, ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9,
          ll10, ll11, ll12, ll13, ll14, ll15):
    

    
    y1 = round(int(sum(ll1[0]) / len(ll1[0])))
    yh1 = round(int(sum(ll1[1]) / len(ll1[1])))
    x1 = round(int(sum(ll1[2]) / len(ll1[2])))
    xw1 = round(int(sum(ll1[3]) / len(ll1[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop1 = gray[y1:yh1, x1:xw1]

 



    y1 = round(int(sum(ll2[0]) / len(ll2[0])))
    yh1 = round(int(sum(ll2[1]) / len(ll2[1])))
    x1 = round(int(sum(ll2[2]) / len(ll2[2])))
    xw1 = round(int(sum(ll2[3]) / len(ll2[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop2 = gray[y1:yh1, x1:xw1]





    y1 = round(int(sum(ll3[0]) / len(ll3[0])))
    yh1 = round(int(sum(ll3[1]) / len(ll3[1])))
    x1 = round(int(sum(ll3[2]) / len(ll3[2])))
    xw1 = round(int(sum(ll3[3]) / len(ll3[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop3 = gray[y1:yh1, x1:xw1]





    y1 = round(int(sum(ll4[0]) / len(ll4[0])))
    yh1 = round(int(sum(ll4[1]) / len(ll4[1])))
    x1 = round(int(sum(ll4[2]) / len(ll4[2])))
    xw1 = round(int(sum(ll4[3]) / len(ll4[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop4 = gray[y1:yh1, x1:xw1]



        

    y1 = round(int(sum(ll5[0]) / len(ll5[0])))
    yh1 = round(int(sum(ll5[1]) / len(ll5[1])))
    x1 = round(int(sum(ll5[2]) / len(ll5[2])))
    xw1 = round(int(sum(ll5[3]) / len(ll5[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop5 = gray[y1:yh1, x1:xw1]



    y1 = round(int(sum(ll6[0]) / len(ll6[0])))
    yh1 = round(int(sum(ll6[1]) / len(ll6[1])))
    x1 = round(int(sum(ll6[2]) / len(ll6[2])))
    xw1 = round(int(sum(ll6[3]) / len(ll6[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop6 = gray[y1:yh1, x1:xw1]




    y1 = round(int(sum(ll7[0]) / len(ll7[0])))
    yh1 = round(int(sum(ll7[1]) / len(ll7[1])))
    x1 = round(int(sum(ll7[2]) / len(ll7[2])))
    xw1 = round(int(sum(ll7[3]) / len(ll7[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop7 = gray[y1:yh1, x1:xw1]

            



    y1 = round(int(sum(ll8[0]) / len(ll8[0])))
    yh1 = round(int(sum(ll8[1]) / len(ll8[1])))
    x1 = round(int(sum(ll8[2]) / len(ll8[2])))
    xw1 = round(int(sum(ll8[3]) / len(ll8[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop8 = gray[y1:yh1, x1:xw1]

        

    y1 = round(int(sum(ll9[0]) / len(ll9[0])))
    yh1 = round(int(sum(ll9[1]) / len(ll9[1])))
    x1 = round(int(sum(ll9[2]) / len(ll9[2])))
    xw1 = round(int(sum(ll9[3]) / len(ll9[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop9 = gray[y1:yh1, x1:xw1]

        

    y1 = round(int(sum(ll10[0]) / len(ll10[0])))
    yh1 = round(int(sum(ll10[1]) / len(ll10[1])))
    x1 = round(int(sum(ll10[2]) / len(ll10[2])))
    xw1 = round(int(sum(ll10[3]) / len(ll10[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop10 = gray[y1:yh1, x1:xw1]


        

    y1 = round(int(sum(ll11[0]) / len(ll11[0])))
    yh1 = round(int(sum(ll11[1]) / len(ll11[1])))
    x1 = round(int(sum(ll11[2]) / len(ll11[2])))
    xw1 = round(int(sum(ll11[3]) / len(ll11[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop11 = gray[y1:yh1, x1:xw1]

        
    
    y1 = round(int(sum(ll12[0]) / len(ll12[0])))
    yh1 = round(int(sum(ll12[1]) / len(ll12[1])))
    x1 = round(int(sum(ll12[2]) / len(ll12[2])))
    xw1 = round(int(sum(ll12[3]) / len(ll12[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop12 = gray[y1:yh1, x1:xw1]

        


    y1 = round(int(sum(ll13[0]) / len(ll13[0])))
    yh1 = round(int(sum(ll13[1]) / len(ll13[1])))
    x1 = round(int(sum(ll13[2]) / len(ll13[2])))
    xw1 = round(int(sum(ll13[3]) / len(ll13[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop13 = gray[y1:yh1, x1:xw1]



        
    y1 = round(int(sum(ll14[0]) / len(ll14[0])))
    yh1 = round(int(sum(ll14[1]) / len(ll14[1])))
    x1 = round(int(sum(ll14[2]) / len(ll14[2])))
    xw1 = round(int(sum(ll14[3]) / len(ll14[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop14 = gray[y1:yh1, x1:xw1]

        

    y1 = round(int(sum(ll15[0]) / len(ll15[0])))
    yh1 = round(int(sum(ll15[1]) / len(ll15[1])))
    x1 = round(int(sum(ll15[2]) / len(ll15[2])))
    xw1 = round(int(sum(ll15[3]) / len(ll15[3])))
    
    cv2.rectangle(gray, (x1, y1), (xw1, yh1), (0), 3)
    crop15 = gray[y1:yh1, x1:xw1]

        





