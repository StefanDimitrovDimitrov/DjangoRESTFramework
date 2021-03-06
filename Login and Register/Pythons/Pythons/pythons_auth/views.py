from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from Pythons.pythons_auth.forms import SignInForm, SignUpForm


def sign_up(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-up.html', context)


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignInForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign-in.html', context)


def sign_out(request):
    logout(request)
    return redirect('index')
