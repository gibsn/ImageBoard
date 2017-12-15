from django.conf.urls import url, include

from . import api

app_name = 'board_api'

urlpatterns = [
    url(r'^new$', api.post_new_message, name='post_new_message'),
    url(r'^edit/(\d+)$', api.edit_message, name='edit_message'),
    url(r'^delete/(\d+)$', api.delete_message, name='delete_message'),
]
