# urls.py
from django.urls import path
from .views import register, additional_info

urlpatterns = [
    path('register/', register, name='register'),
    path('additional_info/<int:user_id>/', additional_info, name='additional_info'),
    # Add other URLs as needed
]
