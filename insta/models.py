from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    name=models.CharField(max_length=50)
    bio=models.TextField(max_length=500,blank=True)
    profile_pic=models.ImageField(upload_to='pictures/')

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ["-pk"]

    def save_image(self):
        '''
        Method to save our images
        '''
        self.save()

    def delete_image(self):
        '''
        Method to delete our images
        '''
        self.delete()

    @property
    def num_liked(self):
        return self.likes.all().count()

    

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user=models.ForeignKey(Profile,related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
class Follow(models.Model):
    follower=models.ForeignKey(Profile,related_name='followers',on_delete=models.CASCADE)
    followed=models.ForeignKey(Profile,related_name='followed',on_delete=models.CASCADE)