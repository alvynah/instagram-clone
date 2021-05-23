from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.welcome, name='welcome'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)