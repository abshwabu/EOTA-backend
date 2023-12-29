from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    ISLAM = 'ISL'
    CRISTIAN ='CRI'
    JEW ='jew'
    TRADITIONAL = 'TRD'
    RELIGION = [
        (ISLAM, 'islam'),
        (CRISTIAN,'cristian'),
        (TRADITIONAL, 'traditional'),
        (JEW, 'jew'),
    ]
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField(max_length=50,null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address=models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")