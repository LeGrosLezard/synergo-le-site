from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


from django import forms
from django.contrib.auth import login as lo 
from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm

from .models import *



def login_view(request):
    """Here we define the login view"""

    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)


    if form.is_valid():
        
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        
        if next:
            return redirect(next)
        return redirect('../../')

    context = {
        'form':form
    }

    return render(request, 'login.html', context)
            

def register(request):
    """Here we define the register view"""


    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)


    if form.is_valid():
        
        print("coucou...")
        user = form.save(commit=False)
        passwordd = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        print(passwordd)
        user.set_password(passwordd)
        print(passwordd)
        user.save()

        new_user = authenticate(username=user.username, password=passwordd)
        login(request, new_user)


        if next:
            return redirect(next)
        return redirect('../../')

    context = {
        'form':form
    }

    return render(request, 'register.html', context)




login_required
def logout_view(request):
    """Here we define logout session"""

    logout(request)
    print("déconnexion")
    return redirect('/')
