from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

# Create your views here.
class Home(TemplateView):
    template_name='home.html'

class RegView(CreateView):
    template_name='reg.html'
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy('h')

class LogView(FormView):
    template_name='log.html'
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            pw=form_data.cleaned_data.get("password")
            ut=form_data.cleaned_data.get("usertype")
            user=authenticate(request,username=un,password=pw,usertype=ut)
            if user:
                if ut=="Store":
                    login(request,user)
                    return redirect('sh')
                else:
                    login(request,user)
                    return redirect("ch")
            else:
                return render(request,'log.html',{"form":form_data})
        else:
            return render(request,'log.html',{"form":form_data})
