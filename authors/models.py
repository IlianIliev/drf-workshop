from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    website = models.URLField()
    bio = models.TextField()
