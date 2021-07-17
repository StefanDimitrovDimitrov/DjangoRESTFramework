from django import views
from django.urls import path

from Pythons.pythons_auth.views import sign_up, sign_in, sign_out

urlpatterns = [
    path('sign-up/', register, name='sign up'),
    path('sign-in/', login, name='sign in'),
    path('sign-out/', logout, name='sign out'),
]
