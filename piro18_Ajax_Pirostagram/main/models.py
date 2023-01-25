from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()

class Comment(models.Model):
    comment = models.CharField(max_length=100)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)