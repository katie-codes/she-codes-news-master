

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about_me = models.TextField(default='')
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True,) 

    def __str__(self):
        return self.username

