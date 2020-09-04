from django import forms
from django.forms import ModelForm 
from .models import NewsStory
from .models import *


choices = [('Coding', 'Coding'), ('Cats', 'Cats'), ('Cupcakes', 'Cupcakes')]

class StoryForm(ModelForm):
     class Meta:
        form_class = 'storyForm'
        model = NewsStory
        fields = ['title', 'pub_date', 'main_content', 'main_image', 'category']
        widgets = {
'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),   

}

