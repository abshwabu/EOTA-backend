from django.urls import path

from api import views

urlpatterns = [
   path('',views.userList.as_view(),name='userList'),
   path('/<int:pk>',views.userDetails.as_view(),name='userDetails'),
]