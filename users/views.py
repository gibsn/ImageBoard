from django.contrib.auth.forms import AuthenticationForm
from django.http import *
from django.shortcuts import render

from .forms import UserForm


def get_profile(request):
    user_form = UserForm()
    initial_dict = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    }

    context = {
        'user_form': UserForm(initial=initial_dict),
    }

    return render(request, "users/profile.html", context)

def sign_in(request):
    context = {
        'sign_in_form': AuthenticationForm(),
    }

    return render(request, "users/signin.html", context)

def sign_up(request):
    return HttpResponse("sign up")
