from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", 'email']


class UpdateProfilePic(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class PaswordReset(PasswordResetForm):

    pass
