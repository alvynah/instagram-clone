from django.http.response import Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from .forms import *
from django.contrib import messages
from .models import Post, Comment, Profile, Follow
from django.http import HttpResponseRedirect
from django.contrib.auth import logout







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

def logout_view(request):
    logout(request,"welcome.html")

@login_required(login_url='/accounts/login/')
def comment(request,post_id):
        current_user=request.user.profile
        post = Post.objects.get(id=post_id)
        user_profile = User.objects.get(username=current_user.user)
        comments = Comment.objects.all()
        if request.method == 'POST':
                form = CommentForm(request.POST, request.FILES)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.post = post
                        comment.user = request.user.profile
                        comment.save()  
                return redirect('welcome')
        else:
                form = CommentForm()
        params = {
        'post': post,
        'form': form,
        'comments': comments,
    }
        return render(request, 'instagram/comment.html',params)
def like_post(request,post_id):
    post = Post.objects.get(pk=post_id)
    is_liked=False
    user=request.user.profile
    try:
        profile=Profile.objects.get(user=user.user)
        print(profile)

    except Profile.DoesNotExist:
        raise Http404()
    if post.likes.filter(id=user.user.id).exists():
        post.likes.remove(user.user)
        is_liked=False
    else:
        post.likes.add(user.user)
        is_liked=True
    return HttpResponseRedirect(reverse('welcome'))