from django.test import TestCase
from .models import Profile,Post,Comment
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user=User(username='alvynah')
        self.user.save()
        self.profile=Profile(user=self.user,name='vee',bio='vee in the house',profile_pic='default.png')
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_saveProfile(self):
        self.profile.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)


# class TestPost(TestCase):
#     def setUp(self):
#         self.profile_test = Profile(name='charles', user=User(username='mikey'))
#         self.profile_test.save()

#         self.image_test = Post(image='default.png', name='test', caption='default test', user=self.profile_test)

#     def test_insatance(self):
#         self.assertTrue(isinstance(self.image_test, Post))

#     def test_save_image(self):
#         self.image_test.save_image()
#         images = Post.objects.all()
#         self.assertTrue(len(images) > 0)

#     def test_delete_image(self):
#         self.image_test.delete_image()
#         after = Profile.objects.all()
#         self.assertTrue(len(after) < 1) 