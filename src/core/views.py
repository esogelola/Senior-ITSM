from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def index(request):
    template = 'index.html'
    context = {
        'title': 'Home',
    }
    return render(request, template, context)


def login(request):
    return render(request, 'login.html', {})


def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        # Return an 'invalid login' error message
        return render(request, 'login.html', {error: "Invalid login"})


def register(request):
    return render(request, 'register.html', {})


def logout(request):
    return render(request, 'logout.html', {})
