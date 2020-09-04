from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories",
    )
    pub_date = models.DateTimeField()
    main_content = models.TextField(default='')
    main_image = models.ImageField(upload_to='images/', null=True) 
    category = models.CharField(max_length=200, default='uncategorised')

