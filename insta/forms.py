from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    fullname=forms.CharField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'password1','password2')
        help_texts = {
            'username': None,
            'password': None,
        }