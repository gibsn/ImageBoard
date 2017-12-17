from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user
from django.http import *
from django.shortcuts import render

from .models import Message
from .forms import NewMessageForm, EditMessageForm

from ImageBoard.settings import get_param


def index(request):
    n = get_param("messages_per_page")
    paginator = Paginator(Message.objects.all().order_by("-datetime"), n)

    page = request.GET.get('page')
    page = page if page else 1

    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        return HttpResponseBadRequest("wrong page number")
    except EmptyPage:
        return HttpResponseNotFound("not found")

    context = {
        'messages': messages,
        'new_message_form': NewMessageForm(),
    }

    return render(request, "board/index.html", context)

def edit_message(request, message_id):
    user = get_user(request)
    message = Message.objects.get(id=message_id)

    if not user == message.author:
        raise PermissionDenied

    context = {
       "edit_message_form": EditMessageForm(instance=message),
       "message_id": message_id,
    }

    return render(request, "board/edit_message.html", context)


