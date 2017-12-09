import datetime
import logging

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import *
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Message
from .forms import NewMessageForm

from ImageBoard.settings import get_param


def index(request):
    n = get_param("messages_per_page")
    paginator = Paginator(Message.objects.all().order_by("-datetime"), n)

    page = request.GET.get('page')
    page = page if page else 1

    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        return HttpResponseBadRequest("bad request")
    except EmptyPage:
        return HttpResponseNotFound("not found")

    context = {
        'messages': messages,
        'new_message_form': NewMessageForm(),
    }

    return render(request, "board/index.html", context)


def post_new_message(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    new_message_form = NewMessageForm(request.POST)
    if new_message_form.is_valid():
        new_message = Message()

        user = request.user
        new_message.author = user if user.is_authenticated else None

        new_message.subject = new_message_form.cleaned_data["subject"]
        new_message.body = new_message_form.cleaned_data["body"]
        new_message.image = request.FILES.get("image")

        dt = datetime.datetime.now()
        new_message.datetime = timezone.make_aware(dt, timezone.get_current_timezone())
        new_message.save()

        return redirect('index')
    else:
        logging.warning("board:new: {} failed to create a new message: {}".format(
            request.META.get("REMOTE_ADDR"),
            ''.join(["{} ({})".format(k, v) for k, v in new_message_form.errors.items()])
        ))

        return HttpResponseBadRequest()
