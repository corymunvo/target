from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('contact.html', views.contact, name='contact'),
    path('catalogue.html', views.catalogue, name='catalogue'), 
    path('arrivals.html', views.arrivals, name='arrivals'), 
    path('shop.html', views.shop, name='shop'),
    path('thankyou.html', views.thankyou, name='thankyou'),
    path('sign-up.html', views.signUp, name='signUp'),

    path('<int:product_id>/shop-single.html', views.shopSingle, name='shopSingle'),
]