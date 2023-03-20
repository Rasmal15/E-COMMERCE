from django.urls import path
from .views import *

urlpatterns=[
    path('shome/',StoreHome.as_view(),name='sh')
]