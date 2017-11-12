from django.forms import ModelForm
from django.contrib.auth import models as auth_models


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = auth_models.User
        fields = ('username', 'first_name', 'last_name', 'email')
