from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'datetime', 'subject')


admin.site.register(Message, MessageAdmin)
