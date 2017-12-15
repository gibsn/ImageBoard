from django.conf.urls import url, include

from . import views

app_name = 'board'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(\d+)$', views.edit_message, name='edit_message'),
]
