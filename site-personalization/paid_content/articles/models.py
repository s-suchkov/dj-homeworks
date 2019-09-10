from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.BooleanField(default=False)


class Article(models.Model):
    name = models.TextField()
    text = models.TextField()
    pay_follows = models.BooleanField()
