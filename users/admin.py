from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.http import *


class MyUserAdmin(UserAdmin):
    def user_change_password(self, request, id, form_url=""):
        user = request.user
        user_to_change = User.objects.get(id=id)

        if (
            user.is_authenticated and not user.is_superuser and
            user_to_change.is_staff and not user == user_to_change
        ):
            return HttpResponseForbidden("forbidden")

        return super().user_change_password(request, id, form_url)

    def change_view(self, request, object_id, form_url="", extra_context=None):
        user = request.user
        user_to_change = User.objects.get(id=object_id)

        if user.is_authenticated and user.is_superuser:
            return super().change_view(request, object_id, form_url, extra_context)

        if user.is_authenticated and user != user_to_change and user_to_change.is_staff:
            return HttpResponseForbidden("forbidden")

        self.fieldsets = (
            (None, {'fields': ('password',)}),
        )

        return super().change_view(request, object_id, form_url, extra_context)


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
