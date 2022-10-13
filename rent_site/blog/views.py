from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(req):
    return render(req,'blog/login.html')

def manga_list(req):
    posts=Post.objects.filter(category="manga")
    return render(req,'blog/manga_list.html',{"posts":posts})
