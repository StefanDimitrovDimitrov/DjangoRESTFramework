from django.urls import path

from pythonauth.views import login_view, logout_view

urlpatterns = (
    path('login/', login_view, name='login user'),
    path('logout/', logout_view, name='logout user'),
)
