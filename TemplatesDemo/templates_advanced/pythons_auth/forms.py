from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#version 1
# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email')
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email', False)
#         if not email:
#             raise forms.ValidationError('Email is required')
#         return email



#version 2
from templates_advanced.pythons_auth.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)