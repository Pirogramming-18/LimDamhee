from django.db import models

class IdeaStar(models.Model):
    star = models.BooleanField(default=False)

class Devtool(models.Model):
    name = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    content = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    interest = models.IntegerField()
    devtool_id = models.ForeignKey(Devtool, related_name="devtool", on_delete=models.CASCADE)
    Devtool = models.CharField(max_length=64)
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')