from django.conf.urls import url, include

from . import api


app_name = "users_api"

urlpatterns = [
    url("^signin$", api.sign_in, name="sign_in"),
    url("^signout$", api.sign_out, name="sign_out"),
    url("^signup$", api.sign_up, name="sign_up"),
    url("^password/change$", api.change_password, name="change_password"),
    url("^profile/change$", api.change_profile, name="change_profile"),
    url("^verify/(\d+)/(.+)$", api.verify, name="verify"),
]
