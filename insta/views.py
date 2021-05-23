from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import Post, Comment, Profile, Follow
from django.http import HttpResponseRedirect, JsonResponse






# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)


            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/accounts/login/')
def welcome(request):
    posts=Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method=='POST':
        form=UploadImageForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)

    else:
        form=UploadImageForm()
    return render(request, 'instagram/index.html',{'posts':posts,'form':form,'users':users})

