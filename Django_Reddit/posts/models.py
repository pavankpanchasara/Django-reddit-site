from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    post_text = models.CharField(max_length=500)
    post_votes = models.IntegerField(default=0)
    post_creation_time = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    comment_votes = models.IntegerField(default=0)
    comment_creation_time = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)