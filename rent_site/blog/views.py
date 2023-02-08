from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, View_Counter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.db import models
from django.views.decorators.cache import cache_page

# class CacheMixin(object):
#     cache_timeout = 60

#     def get_cache_timeout(self):
#         return self.cache_timeout

#     def dispatch(self, *args, **kwargs):
#         return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)


def home(req):
    return render(req, 'blog/login.html')


def manga_list(req):
    posts = Post.objects.filter(category="manga")
    return render(req, 'blog/manga_list.html', {"posts": posts})


class MangaListView(ListView):
    queryset = Post.objects.filter(category="manga")
    ordering = ['-date_added']
    context_object_name = 'posts'
    template_name = 'blog/manga_list.html'  # <app>/<model>_<viewtype>.html
    paginate_by = 2


class MangaDetailView(DetailView):
    model = Post
    template_name = 'blog/manga_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = str(self.get_object())
        try:
            view_obj = View_Counter.objects.get(post=self.get_object())
        except:
            view_obj = View_Counter(post=self.get_object(), views=0)
            view_obj.save()
        if not self.request.session.get('counted'+title):
            view_obj.views += 1
            view_obj.save()
            self.request.session['counted'+title] = True
        if self.request.user.is_anonymous:
            print(self.request.session.get_expiry_age())
        print(self.request.user)
        print('a')
        context['views'] = view_obj.views
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category']

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


class UserPostListView(ListView):
    ordering = ['-date_added']
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_post_list.html'
    paginate_by = 2

    def get_queryset(self):

        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return Post.objects.filter(author=user).order_by('-date_added')


def view_counter(req, **kwargs):
    id = kwargs.get('pk')
    view_obj = View_Counter.objects.get(post__pk=id)
