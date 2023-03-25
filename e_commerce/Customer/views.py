from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from Store.models import Products
from .models import *
from .forms import *
from django.contrib import messages
from Store.forms import ProductForm
from django.urls import reverse_lazy

# Create your views here.
class CustomerHome(TemplateView):
    template_name='customerhome.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.all()
        return context

class ProductView(TemplateView):
    template_name='product.html'
    def get_context_data(self, **kwargs):
        id=kwargs.get('pk')
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.get(id=id)
        context["form"]=ReviewForm()
        context['review']=Review.objects.all()
        context['pst']=Purchase.objects.filter(user=self.request.user)
        return context
def addreview(request,*args,**kwargs):
    if request.method=="POST":
        id=kwargs.get('pid')
        product=Products.objects.get(id=id)
        user=request.user
        cmnt=request.POST.get("comment")
        Review.objects.create(product=product,user=user,comment=cmnt)
        return redirect('ch')


def addcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    mobile=Products.objects.get(id=id)
    user=request.user
    if Cart.objects.filter(status="carted"):
        messages.success(request,"alredy carted")
        return redirect('ch')
    else:
        Cart.objects.create(mobile=mobile,user=user,status="carted")
        return redirect('ch')
        


class MyCart(TemplateView):
    template_name='mycart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Cart.objects.filter(user=self.request.user)
        # context["staus"]=Cart.status=="purchased"
        return context

class Buy(TemplateView):
    template_name='buy.html'
    def get_context_data(self, **kwargs):
        id=kwargs.get('pid')
        context= super().get_context_data(**kwargs)
        context["data"]=Products.objects.get(id=id)
        context["form"]=PurchaseForm()
        return context

def buyitem(request,*args,**kwargs):
    id=kwargs.get("pid")
    mobile=Products.objects.get(id=id)
    user=request.user
    city=request.POST.get('city')
    post=request.POST.get('post')
    pin=request.POST.get('pin')
    quantity=request.POST.get('quantity')
    Purchase.objects.create(city=city,post=post,pin=pin,quantity=quantity,mobile=mobile,user=user)
    ucart=Cart.objects.get(mobile=id)
    ucart.status="purchased"
    ucart.save()
    return redirect('ch')


class Myorder(TemplateView):
    template_name='myorders.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Purchase.objects.filter(user=self.request.user)
        return context