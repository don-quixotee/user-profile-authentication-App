from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import Group
from django.contrib import messages
from  django.contrib.auth.decorators import login_required


from . import models
from .decorators import *
from .forms import CreateUserFrom




###########################################################################################################################
# #########################################################################################################################

@unauthenticated_user
def registerPage(request):
    
    form = CreateUserFrom()
    
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')


    context = {'form':form}
    return render(request, 'register.html', context)

@unauthenticated_user

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is wrong')


    context= {}
    return render(request, 'login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles = ['customer'])
def userPage(request):
    
    context = {}
    return render(request, 'user.html', context)



@login_required(login_url='login')
@admin_only
def home(request):
    context = {}
    return render(request, 'home.html', context = {})


@login_required
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    context = {}
    return render (request, 'account_settings.html', context)

