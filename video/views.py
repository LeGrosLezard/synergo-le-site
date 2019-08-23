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
#We call this function, it displaying video !
from .views_function import displaying_video_user
def video_capture(request):
    """Here we displaying video"""

    #Current user
    pseudo = request.user

    #We recup from database videos names
    #of users (In big we ask database what video from media is to user)
    video = recup_video_user(pseudo)
    video = list(video)

    #Here we recup POST method.
    if request.method == "POST":
        
        #First we ask the video name.
        video_name = request.POST.get('video_name')
        #Pause video

        #Stop video

        if video_name:
            #we displaying this video.
            displaying_video_user(video_name)
            return HttpResponse("OK")

    return render(request, 'video_capture.html', {"user":pseudo,
                                                  "liste":video})






















    
