from django.urls import path
from .views import *

urlpatterns=[
    path('shome/',StoreHome.as_view(),name='sh'),
    path('addpro/',AddProduct.as_view(),name='addp'),
    path('mypro/',MyProducts.as_view(),name='myp'),
    path('updatepro/<int:pk>/',UpdateProduct.as_view(),name='updatepro'),
    path('deletepro/<int:pk>/',DeleteProduct.as_view(),name='deletepro'),
]