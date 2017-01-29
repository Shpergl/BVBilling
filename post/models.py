from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from extuser.models import MyUser as User
from django.db import models

#User = get_user_model()
SHORT_TEXT_LEN = 100
class Post(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    authorName = models.CharField(unique=True, max_length=200, default='')

    def __str__(self):
        return self.title

    def get_cut(self):
        if self.text > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        return self.text

class Comments(models.Model):
    text = models.TextField(verbose_name="Add Text")
    post = models.ForeignKey(Post)



