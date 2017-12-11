from django.forms import ModelForm, PasswordInput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings


class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["picture"].required = False

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'picture')


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["picture"].required = False

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'picture')
#
#
# class UserAdminForm(UserChangeForm):
