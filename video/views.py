import os
import shutil
import cv2 #for database
from django.shortcuts import render #for render
from django.http import HttpResponse #for response
from django.http import HttpResponseRedirect #for redirecting

import threading

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
               
            #path video media
            path1 = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\synergo\media\video_upload\{}"
            path2 = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\static\video\{}"
            file = str(file)
            #we import video from media to static for the template
            shutil.copyfile(path1.format(str(file[13:])), path2.format(str(file[13:])))

            #path text_video
            #we import video from media to static for the template
            path3 = r"C:\Users\jeanbaptiste\Desktop\boboDancer\env\synergo\static\video_texte\{}"
            #convert path text for analysis object .mp4 to .txt
            file_txt = str(file)
            file_txt = file_txt[13:-3] + "txt" #13:3 -> because real name is video_upload\video2_IjhobwF.mp4
            file = open(path3.format(str(file_txt)), "w")

            #And we return to video watch template
            return HttpResponseRedirect('/video/video_capture/')
    
    return render(request, 'telechargement_video.html', {"form":form})





#We call function user_video from database for recup names of video
from database.video.users_video import recup_video_user
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
        video_name = request.POST.get('video_name')
        #First we ask the video name.
        if video_name:
            path1 = "/static/video/{}".format(str(video_name[13:]))
            path2 = "/static/video_texte/{}".format(str(video_name[13:]))

            return HttpResponse(str(path1))
  

            
 
    return render(request, 'video_capture.html', {"user":pseudo,
                                                  "liste":video})





#We call this function, it displaying video !
from .views_function import displaying_video_user
#We call this function for reading the current video analysis
from .views_function import displaying_video_user
def video_fantome(request):
    
    if request.method == "POST":
        video_name = request.POST.get('video_name')

        if video_name:
            print(video_name, "videoooooooooooooooooooo")
            #we displaying this video.
            displaying_video_user(video_name)
            return HttpResponse('ok')















    
