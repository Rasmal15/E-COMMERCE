from django.urls import path
from .views import *

urlpatterns=[
    path('chome/',CustomerHome.as_view(),name='ch'),
    path('mycart/',MyCart.as_view(),name='mycart'),
    path('pro/<int:pk>',ProductView.as_view(),name='pro'),
    path('addcart/<int:pid>',addcart,name='addcart'),
]