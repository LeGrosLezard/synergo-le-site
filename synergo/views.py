from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def garde(request):
    return render(request, 'garde.html')

def transition(request):
    return render(request, 'transition.html')

def transition_login(request):
    return render(request, 'transition_login.html')

def transition_register(request):
    return render(request, 'transition_register.html')

def menu(request):
    return render(request, 'menu.html')

def essais_home(request):
    return render(request, 'essais_home.html')
