from django.contrib import admin
from django.urls import path
from .views import (
    MangaListView,
    MangaDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView)
urlpatterns = [
    path("", MangaListView.as_view(), name="manga-list"),
    path("manga/<int:pk>", MangaDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]
