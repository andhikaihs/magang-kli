from django import forms
# from django.contrib.auth.models import User
from .models import Profile

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['full_name', 'nip', 'role', 'email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'user']
