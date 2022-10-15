
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    category=models.CharField(max_length=20,default="manga")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
