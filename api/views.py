from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, UserProfileForm
from .models import UserProfile
from formtools.wizard.views import SessionWizardView

def home(request):
    return render(request, 'home.html')

# def register(request):
#     if request.method == 'POST':
#         registration_form = RegistrationForm(request.POST)
#         if registration_form.is_valid():
#             user = registration_form.save()
#             # Create UserProfile instance for the new user
#             UserProfile.objects.create(user=user)
#             login(request, user)
#             return redirect('user_profile')
#     else:
#         registration_form = RegistrationForm()
#     return render(request, 'register.html', {'form': registration_form})

# def user_profile(request):
#     if request.method == 'POST':
#         try:
#             user_profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
#         except ValueError:
#             # Create a new UserProfile if it doesn't exist
#             user_profile_form = UserProfileForm(request.POST)
#         if user_profile_form.is_valid():
#             user_profile_form.save()
#             return redirect('home')
#     else:
#         try:
#             user_profile_form = UserProfileForm(instance=request.user.userprofile)
#         except ValueError:
#             user_profile_form = UserProfileForm()
#     return render(request, 'user_profile.html', {'form': user_profile_form})
class RegistrationWizardView(SessionWizardView):
    form_list = [RegistrationForm,UserProfileForm]
    template_name = 'user_profile.html'

    def done(self, form_list, **kwargs):
        registration_data = {}
        for form in form_list:
            registration_data.update(form.cleaned_data)