from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('authors.Author')
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    liked_by = models.ManyToManyField(User, related_name='likes')
