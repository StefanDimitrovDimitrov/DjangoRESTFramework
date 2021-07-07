

from django.contrib.auth import logout, authenticate, login
from django.db import transaction
from django.shortcuts import render, redirect

from templates_advanced.pythons_auth.forms import RegisterForm, ProfileForm

# @transaction.atomic
def register_view(request):
    if request.method == "GET":
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/register.html', context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('index')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }

        return render(request, 'auth/register.html', context)


def login_view(request):
    username = 'IvanDimitrov'
    password = '12345qwert!'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('index')

    return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')
