from django.contrib import admin
from django.urls import path
from .views import (
    MangaListView,
    MangaDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    UserPostListView)
from django.views.decorators.cache import cache_page
from .decorators import conditional_cache

urlpatterns = [
    path("", (MangaListView.as_view()), name="manga-list"),
    path("manga/<int:pk>", conditional_cache(decorator=cache_page(600))
         (MangaDetailView.as_view()), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>', cache_page(60 * 15)
         (UserPostListView.as_view()), name='user-posts'),
    
]
