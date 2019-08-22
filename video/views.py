from django.shortcuts import render
from django.http import HttpResponse
import cv2

#We importing form and model from
#models.py and forms.py
#We return the form,
#We recup the post and if it's valid we uploading it
#on the MEDIA folder.


from .forms import video_upload_form
from .models import video_upload
from .views_function import search_video_name
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
            
            #Here we see if the video name already exists or not
            present_video = search_video_name(name_video)
            
            #If name exists so we ask user to changes it
            #and register it into database
            if present_video is None:
                return HttpResponse("rename")
            
            #If not exists we save it on media folder.
            #and register it into database
            else:
                newdoc = video_upload(docfile = request.FILES['docfile'])
                newdoc.save()


    
    return render(request, 'telechargement_video.html', {"form":form})



def video_capture(request):

    pseudo = request.user





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

    return render(request, 'video_capture.html', )






















    
