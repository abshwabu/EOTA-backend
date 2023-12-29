# views.py
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import UserProfile
from .forms import UserProfileForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username already exists
        if UserProfile.objects.filter(username=username).exists():
            # Handle the case where the username is already taken
            return render(request, 'register.html', {'error_message': 'Username is already taken. Please choose a different one.'})

        try:
            # Create a new user if the username is unique
            user_profile = UserProfile.objects.create(username=username, password=password)
            return redirect('additional_info', user_id=user_profile.id)
        except IntegrityError:
            # Handle any other IntegrityError that might occur
            return render(request, 'register.html', {'error_message': 'An error occurred during registration. Please try again.'})

    return render(request, 'register.html')


# ... rest of the code ...


# views.py
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def additional_info(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page or any other desired page
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'additional_info.html', {'form': form, 'user_id': user_id})
