from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(User)

    def __str__(self):
        return self.title
