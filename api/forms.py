from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):
    Bool_options = [{True:'Ok'}, {False:'No thanks'}]
    Enter_more_details = forms.BooleanField(
        widget=forms.RadioSelect(choices=Bool_options)
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','Enter_more_details']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'occupation', 'religion']
