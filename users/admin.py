from django.core.exceptions import PermissionDenied
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.backends import ModelBackend
from django.http import *
from django.conf import settings


class MyUserAdmin(UserAdmin):
    def user_change_password(self, request, id, form_url=""):
        user = get_user(request)
        user_to_change = get_user_model().objects.get(id=id)

        if (
            user.is_authenticated and not user.is_superuser and
            user_to_change.is_staff and not user == user_to_change
        ):
            raise PermissionDenied

        return super().user_change_password(request, id, form_url)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        user = get_user(request)
        user_to_change = get_user_model().objects.get(id=object_id)

        if user.is_authenticated and user.is_superuser:
            return super().change_view(request, object_id, form_url, extra_context)

        if user.is_authenticated and user != user_to_change and user_to_change.is_staff:
            raise PermissionDenied

        self.fieldsets = (
            (None, {'fields': ('password',)}),
            (None, {'fields': ('is_staff', 'groups',)}),
        )

        return super().change_view(request, object_id, form_url, extra_context)


admin.site.register(get_user_model(), MyUserAdmin)
