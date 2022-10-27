from django.shortcuts import render


def index(request):
    template =     'index.html'
    context = {
        'title': 'Home',
    }
    return render(request, template, context)
    



def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def logout(request):
    return render(request, 'logout.html', {})

