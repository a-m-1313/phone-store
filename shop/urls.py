from django.urls import include, path
from . import views



urlpatterns = [
    path('mobile/<slug:slug>', views.product_detail, name='product_detail'),
    path('', views.mobile_list, name='mobile_list'),
   
   
]
