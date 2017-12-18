from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.http import *
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from .forms import UserProfileForm, SignUpForm


def sign_in(request):
    sign_in_form = AuthenticationForm(data=request.POST)
    if not sign_in_form.is_valid():
        return render(request, "error.html", {"form": sign_in_form})

    username = sign_in_form.cleaned_data['username']
    password = sign_in_form.cleaned_data['password']

    user = authenticate(username=username, password=password)
    if user is None:
        return redirect('users:sign_in')

    login(request, user)

    return redirect('index')

def sign_up(request):
    sign_up_form = SignUpForm(request.POST)
    if not sign_up_form.is_valid():
        return render(request, "error.html", {"form": sign_up_form})

    new_user = sign_up_form.save(commit=False)
    new_user.is_active = False
    new_user.image = request.FILES.get("image")
    new_user.save()

    token = PasswordResetTokenGenerator().make_token(new_user)
    verification_link = "https://{}/api/users/verify/{}/{}".format(
        get_current_site(request).domain,
        new_user.id,
        token,
    )

    new_user.email_user("email verification", verification_link, from_email=settings.EMAIL_HOST_USER)

    return redirect('index')

def sign_out(request):
    logout(request)
    return redirect('index')

def change_password(request):
    form = SetPasswordForm(request.user, request.POST)
    if not form.is_valid():
        return render(request, "error.html", {"form": form})

    form.save()
    update_session_auth_hash(request, form.user)
    authenticate(request)
    login(request, form.user)
    return redirect('index')

def change_profile(request):
    form = UserProfileForm(request.POST, instance=request.user)
    if not form.is_valid():
        return render(request, "error.html", {"form": form})

    user_edited = form.save(commit=False)
    if request.FILES.get("image"):
        user_edited.image = request.FILES.get("image")

    user_edited.save()

    return redirect('users:profile')

def verify(request, uid, token):
    user = get_user_model().objects.get(pk=uid)
    if user == None:
        return HttpResponseBadRequest("no such user")

    if not PasswordResetTokenGenerator().check_token(user, token):
        return HttpResponseBadRequest("invalid token")

    user.is_active = True
    user.save()

    authenticate(request)
    login(request, user)

    return redirect('index')
