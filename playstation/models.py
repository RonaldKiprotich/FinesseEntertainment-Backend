from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField



# Create your models here.


class Profile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profilephoto = CloudinaryField('image')
    contact = models.IntegerField(null=True)
   
    

    def __str__(self):
        return self.user.username


    
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    fullname = models.CharField(blank=True, max_length=150)
    nickname = models.CharField(blank=True, max_length=150) 
    email = models.CharField(blank=True, max_length=150)
    


