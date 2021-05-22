from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    bio=models.TextField(max_length=500,blank=True)
    profile_pic=models.ImageField(upload_to='pictures/')

