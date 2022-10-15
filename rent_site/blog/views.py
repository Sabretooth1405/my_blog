from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.db import models

def home(req):
    return render(req,'blog/login.html')

def manga_list(req):
    posts=Post.objects.filter(category="manga")
    return render(req,'blog/manga_list.html',{"posts":posts})


class MangaListView(ListView):
    queryset= Post.objects.filter(category="manga")
    ordering=['-date_added']
    context_object_name = 'posts'
    template_name='blog/manga_list.html' # <app>/<model>_<viewtype>.html

class MangaDetailView(DetailView):
    model=Post
    template_name='blog/manga_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
