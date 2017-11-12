from django.contrib.auth import logout
from django.http import *
from django.shortcuts import redirect


def sign_in(request):
    return HttpResponseServerError()

def sign_up(request):
    return HttpResponseServerError()

def sign_out(request):
    logout(request)
    return redirect('index')
