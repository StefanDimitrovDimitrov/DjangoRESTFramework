from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    username = 'IvanDimitrov'
    password = '12345qwert!'
    user = authenticate(username=username,password=password)
    if user:
        login(request, user)
        return redirect('index')

    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')