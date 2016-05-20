"""This module contains DB models"""
from django.db import models
from django.utils import timezone
from core_app import utils
from hashlib import md5


# create our model Comment

class Comment(models.Model):

    url = models.CharField(max_length=1000, default='')
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=timezone.now)