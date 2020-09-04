
from django.urls import path
from .views import CreateAccountView
from .views import ChangeAccountView
from .views import AccountView
from .views import AuthorView

from django.conf import settings 
from django.conf.urls.static import static 




app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    path('change-account/<int:pk>', ChangeAccountView.as_view(),name='changeAccount'),
    path('view-account/<int:pk>', AccountView.as_view(),name='viewAccount'),
    path('author/<int:pk>', AuthorView.as_view(),name='author'),

]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)