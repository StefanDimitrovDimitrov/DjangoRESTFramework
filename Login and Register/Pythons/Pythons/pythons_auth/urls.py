from django import views
from django.urls import path

from Pythons.pythons_auth.views import sign_up, sign_in, sign_out

urlpatterns = [
    path('sign-up/', sign_up, name='sign up'),
    path('sign-in/', sign_in, name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
]
