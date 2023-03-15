from django.shortcuts import render
from django.views.generic import View,TemplateView,CreateView
from .forms import *
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name='home.html'

class RegView(CreateView):
    template_name='reg.html'
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy('h')