from servicii import forms
from django.forms import ModelForm
from users.models import UserModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"