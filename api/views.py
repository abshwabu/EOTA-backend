from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import UserSerializer
# Create your views here.

class userList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class userDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

