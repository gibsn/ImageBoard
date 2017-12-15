import datetime
import logging

from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user
from django.http import *
from django.shortcuts import redirect
from django.utils import timezone

from .models import Message
from .forms import NewMessageForm, EditMessageForm


def post_new_message(request):
    user = get_user(request)

    new_message_form = NewMessageForm(request.POST)
    if not new_message_form.is_valid():
        logging.warning("board:new: {} failed to create a new message: {}".format(
            request.META.get("REMOTE_ADDR"),
            ''.join(["{} ({})".format(k, v) for k, v in new_message_form.errors.items()])
        ))

        return HttpResponseBadRequest()

    new_message = new_message_form.save(commit=False)

    new_message.author = user if user.is_authenticated else None
    new_message.subject = new_message_form.cleaned_data["subject"]
    new_message.body = new_message_form.cleaned_data["body"]
    new_message.image = request.FILES.get("image")

    dt = datetime.datetime.now()
    new_message.datetime = timezone.make_aware(dt, timezone.get_current_timezone())

    new_message.save()

    return redirect('index')

def delete_message(request, message_id):
    user = get_user(request)
    message = Message.objects.get(id=message_id)

    if not user == message.author:
        raise PermissionDenied

    message.delete()

    return redirect('index')

def edit_message(request, message_id):
    user = get_user(request)
    message = Message.objects.get(id=message_id)

    if not user == message.author:
        raise PermissionDenied

    edit_message_form = EditMessageForm(request.POST, instance=message)
    if not edit_message_form.is_valid():
        return HttpResponseBadRequest()

    edited_message = edit_message_form.save(commit=False)
    edited_message.is_edited = True
    edited_message.image = request.FILES.get("image")
    edited_message.save()

    return redirect('index')
