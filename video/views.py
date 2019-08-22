from django.shortcuts import render


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
            print("ouiiiiiiiiiii")

            newdoc = video_upload(docfile = request.FILES['docfile'])
            newdoc.save()
           
            print("coucou")

        
    return render(request, 'telechargement_video.html', {"form":form})
