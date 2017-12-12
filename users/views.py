from django.contrib.auth import get_user
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.http import *
from django.shortcuts import render

from .forms import UserProfileForm, SignUpForm


def get_profile(request):
    user = get_user(request)

    initial_dict = {
        'username':   user.username,
        'first_name': user.first_name,
        'last_name':  user.last_name,
        'email':      user.email,
        'picture':    user.picture,
    }

    context = {
        'user_form': UserProfileForm(initial=initial_dict),
    }

    return render(request, "users/profile.html", context)

def change_password(request):
    context = {
        'password_form': SetPasswordForm(request.user),
    }

    return render(request, "users/change_password.html", context)

def sign_in(request):
    context = {
        'sign_in_form': AuthenticationForm(),
    }

    return render(request, "users/signin.html", context)

def sign_up(request):
    context = {
        'sign_up_form': SignUpForm(),
    }

    return render(request, "users/signup.html", context)

