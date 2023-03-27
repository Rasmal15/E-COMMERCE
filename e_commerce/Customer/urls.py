from django.urls import path
from .views import *

urlpatterns=[
    path('chome/',CustomerHome.as_view(),name='ch'),
    path('mycart/',MyCart.as_view(),name='mycart'),
    path('myorder/',Myorder.as_view(),name='myo'),
    path('pro/<int:pk>',ProductView.as_view(),name='pro'),
    path('addcart/<int:pid>',addcart,name='addcart'),
    path('buyitem/<int:pid>',buyitem,name='buyitem'),
    path('buy/<int:pid>',Buy.as_view(),name='buy'),
    path('review/<int:pid>',addreview,name='addr'),
    path('delcart/<int:pid>',delcart,name='delcart'),

]   