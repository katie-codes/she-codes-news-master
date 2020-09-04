from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm
)
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        form_class = 'storyForm'
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name', 'about_me', 'profile_picture',]


    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        form_class = 'storyForm'
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name', 'about_me', 'profile_picture',]


