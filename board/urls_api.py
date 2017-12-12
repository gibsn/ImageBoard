from django.conf.urls import url, include

from . import views

app_name = 'board_api'

urlpatterns = [
    url(r'^new$', views.post_new_message, name='post_new_message'),
    url(r'^delete/(\d+)$', views.delete_message, name='delete_message'),
]
