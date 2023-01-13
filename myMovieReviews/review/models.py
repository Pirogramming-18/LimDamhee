from django.conf import settings
from django.db import models
from django.utils import timezone


class Review(models.Model):
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=30, default='')
    director = models.CharField(max_length=20)
    character = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    star = models.FloatField()
    time = models.CharField(max_length=20)
    content = models.TextField()