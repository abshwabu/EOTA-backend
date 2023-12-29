# models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True)
    religion = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username
