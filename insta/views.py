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

@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    print(followers)
    return render(request, 'instagram/user_profile.html', params)

@login_required(login_url='login')
def profile(request, username):
    posts = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'posts': posts,

    }
    return render(request, 'instagram/profile.html', params)