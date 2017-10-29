from django.forms import ModelForm

from . import models


class NewMessageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["image"].required = False

    class Meta:
        model = models.Message
        fields = ('subject', 'body', 'image',)
