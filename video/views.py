from django.shortcuts import render
from django.http import HttpResponse
import cv2
from django.http import HttpResponseRedirect

#We importing form and model from
#models.py and forms.py
#We return the form,
#We recup the post and if it's valid we uploading it
#on the MEDIA folder.


from .forms import video_upload_form
from .models import video_upload
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
            #And we return to video watch template
            return HttpResponseRedirect('/video/video_capture/')
    
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






















    
