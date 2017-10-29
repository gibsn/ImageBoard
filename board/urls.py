from django.conf.urls import url, include

from . import views

app_name = 'board'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
