from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    post_header = models.CharField(max_length=200,default="First Post")
    post_text = models.CharField(max_length=500)
    post_votes = models.IntegerField(default=0)
    post_creation_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_header

    def was_published_recently(self):
        return self.post_creation_time >= timezone.now() - datetime.timedelta(days = 1)

class Comment(models.Model):
    comment_text = models.CharField(max_length=500)
    comment_votes = models.IntegerField(default=0)
    comment_creation_time = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text