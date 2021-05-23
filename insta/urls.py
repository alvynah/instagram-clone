from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.welcome, name='welcome'),
    path('comment/<post_id>', views.comment, name='comment'),    

   

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)