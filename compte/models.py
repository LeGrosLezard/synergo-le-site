from django.db import models


class compte(models.Model):

    nom = models.CharField(max_length=255)
    
    password = models.CharField(max_length=255)
    
    email = models.EmailField(max_length=255)
    


    def __str__(self):
        return self.email


