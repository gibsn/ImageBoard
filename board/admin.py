from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'datetime', 'subject', 'body')

    # sorry
    def has_change_permission(self, request, obj=None):
        if request.path == "/admin/" or request.path == "/admin/board/message/":
            return True
        else:
            return super().has_change_permission(request, obj)


admin.site.register(Message, MessageAdmin)
