from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=64) 
    access_token = models.CharField(max_length=256)
    adsid = models.CharField(max_length=64)

    def __str__(self):
        return self.email
    