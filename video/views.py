import cv2 #for database
from django.shortcuts import render #for render
from django.http import HttpResponse #for response
from django.http import HttpResponseRedirect #for redirecting




#We importing form for uploading
from .forms import video_upload_form
#We importing models for uploading
from .models import video_upload
#We importing database for insert (video <-> user) uploading
from database.video.users_video import current_user_video


def telechargement_video(request):
    """Here we recup post method
    from user. We recup the download file"""

    #Recup current user connected
    pseudo = request.user

    #We call form for downloading
    form = video_upload_form(request.POST, request.FILES)

    #If we get post method (user submit his folder)
    if request.method == "POST":
        
        #If the form is valid
        if form.is_valid():
            
            #recup the file
            name_video = request.FILES['docfile']
            #Clean it
            form.cleaned_data['docfile'].name
            # we save it on media folder.
            #and register it into database
            newdoc = video_upload(docfile = request.FILES['docfile'])
            newdoc.save()
            
            #And now we insert it into database
            file = newdoc.docfile
            current_user_video(pseudo, file)
            
            #And we return to video watch template
            return HttpResponseRedirect('/video/video_capture/')
    
    return render(request, 'telechargement_video.html', {"form":form})


#We call function user_video from database for recup names of video
from database.video.users_video import recup_video_user
def video_capture(request):

    pseudo = request.user
    video = recup_video_user(pseudo)
    video = list(video)



    if request.method == "POST":
        video = cv2.VideoCapture(0)
        while(True):
            ret, frame = video.read()
            cv2.imshow('FACE', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        video.release()
        cv2.destroyAllWindows()
            
        return HttpResponse("OK")

    return render(request, 'video_capture.html', {"user":pseudo,
                                                  "liste":video})






















    
