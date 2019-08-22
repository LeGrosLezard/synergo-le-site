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
def telechargement_video(request):

    pseudo = request.user

    form = video_upload_form(request.POST, request.FILES)

    if request.method == "POST":

        if form.is_valid():

            newdoc = video_upload(docfile = request.FILES['docfile'])
            newdoc.save()
        
    return render(request, 'telechargement_video.html', {"form":form})



def video_capture(request):
    
    video = cv2.VideoCapture(0)
    while(True):
        ret, frame = video.read()
        cv2.imshow('FACE', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    video.release()
    cv2.destroyAllWindows()
        
    return HttpResponse("OK")























    
