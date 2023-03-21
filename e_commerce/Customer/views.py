from django.shortcuts import render
from django.views.generic import View,TemplateView
from Store.models import Products

# Create your views here.
class CustomerHome(TemplateView):
    template_name='customerhome.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.all()
        return context