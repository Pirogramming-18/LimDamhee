from django.conf import settings
from django.db import models
from django.utils import timezone


class Review(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=20)
    character = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    star = models.FloatField()
    time = models.CharField(max_length=20)
    content = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title