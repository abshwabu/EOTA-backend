from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(choices=[
        (18, '18-24'),
        (25, '25-34'),
        (35, '35-44'),
        # Add more age ranges as needed
    ])
    occupation = models.CharField(max_length=50, choices=[
        ('student', 'Student'),
        ('employed', 'Employed'),
        ('self-employed', 'Self-employed'),
        # Add more occupations as needed
    ])
    religion = models.CharField(max_length=50, blank=True)
    # Add other additional fields as needed

