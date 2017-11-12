from django.conf.urls import url, include

from . import views

app_name = "users"

urlpatterns = [
    url(r'^profile$', views.get_profile, name='profile'),
    url(r'^signin$', views.sign_in, name='sign_in'),
    url(r'^signup$', views.sign_up, name='sign_up'),
]
