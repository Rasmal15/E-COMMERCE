from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustUser


class RegForm(UserCreationForm):
    class Meta:
        model=CustUser
        fields=[
            "first_name",
            "last_name",
            "email",
            "image",
            "address",
            "phone",
            "usertype",
            "username",
            "password1",
            "password2",
        ]
