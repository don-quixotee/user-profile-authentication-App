from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile


class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class CustomerForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


