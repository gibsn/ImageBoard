from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user, get_user_model, update_session_auth_hash
from django.http import *
from django.shortcuts import render, redirect

from .forms import UserProfileForm, SignUpForm


def get_profile(request):
    user = get_user(request)

    if request.method == 'GET':
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

    form = UserProfileForm(request.POST, instance=user)
    if form.is_valid():
        user_edited = form.save(commit=False)
        user_edited.picture = request.FILES.get("picture")
        user_edited.save()

        return redirect('users:profile')

    return HttpResponseBadRequest("bad request")

def change_password(request):
    user = get_user(request)

    if request.method == 'GET':
        context = {
            'password_form': SetPasswordForm(user),
        }

        return render(request, "users/change_password.html", context)

    form = SetPasswordForm(user, request.POST)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        authenticate(request)
        login(request, form.user)
        return redirect('index')

    return HttpResponseBadRequest("bad request")

def sign_in(request):
    context = {
        'sign_in_form': AuthenticationForm(),
    }

    return render(request, "users/signin.html", context)

def sign_up(request):
    return HttpResponse("sign up")
