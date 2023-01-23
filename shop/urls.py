from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='hm'),
    path('shop.html', views.shop, name='shop'),
    path('search.html', views.search, name='search'),
    # path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('contact.html', views.contact, name='contact'),
    path('<slug:c_slug>/', views.home, name='prodcat'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetails, name='details'),
]