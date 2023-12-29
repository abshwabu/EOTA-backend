# views.py
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_profile = UserProfile.objects.create(username=username, password=password)
        return redirect('additional_info', user_id=user_profile.id)
    return render(request, 'register.html')

def additional_info(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or any other desired page
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'additional_info.html', {'form': form})
