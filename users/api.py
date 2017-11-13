from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import *
from django.shortcuts import redirect


def sign_in(request):
    sign_in_form = AuthenticationForm(data=request.POST)
    if not sign_in_form.is_valid():
        return redirect('users:sign_in')

    username = sign_in_form.cleaned_data['username']
    password = sign_in_form.cleaned_data['password']

    user = authenticate(username=username, password=password)
    if user is None:
        return redirect('users:sign_in')

    login(request, user)

    return redirect('index')

def sign_up(request):
    return HttpResponseServerError()

def sign_out(request):
    logout(request)
    return redirect('index')
