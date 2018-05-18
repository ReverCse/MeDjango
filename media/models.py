from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    filename = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
