import cv2

PATH_VIDEO = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\synergo\media\{0}"


def displaying_video_user(video_name):

    #Create video object with path video of click of user
    video = cv2.VideoCapture(PATH_VIDEO.format(video_name))

    ok = True
    
    #Loop while True read this:
    while(True):
        
        #If key push (but it don't serve here)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            ok = False
        
        if cv2.waitKey(1) & 0xFF == ord('b'):
            ok = True
            
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

        if ok is True:
            #Picture by picture reading
            ret, frame = video.read()
            frame = cv2.resize(frame, (600, 400))
        
            #Displaying it
            cv2.imshow('VIDEO', frame)
            
    #I don't know
    video.release()
    #Destroy all windowd
    cv2.destroyAllWindows()

