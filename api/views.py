from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect('user_profile')
    else:
        registration_form = RegistrationForm()
    return render(request, 'register.html', {'form': registration_form})

def user_profile(request):
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_profile_form.is_valid():
            user_profile_form.save()
            return redirect('home')  # Redirect to home or any desired page
    else:
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'user_profile.html', {'form': user_profile_form})
