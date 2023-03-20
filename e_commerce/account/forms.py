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

class LogForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
    # options=(
    #     ("Store","Store"),
    #     ("Customer","Customer"),
    # )
    # usertype=forms.ChoiceField(choices=options)

    
