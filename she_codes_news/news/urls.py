from django.urls import path
from . import views
from .views import *
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    # int pk refers to the id of the story, ie news/14
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
] 

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

