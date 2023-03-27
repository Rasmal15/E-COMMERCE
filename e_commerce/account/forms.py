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
            "address",
            "phone",
            "usertype",
            "username",
            "password1",
            "password2",
        ]
        help_texts={
            'username':None
        }
class LogForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"input-box","placeholder":"username"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"input-box","placeholder":"password"}))

    
