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
    path('thankyou.html', views.thank_you, name='thankyou'),
    path('sign-up.html', views.sign_up, name='signUp'),
    path('products.csv', views.csv_products, name='csvProducts'),
    path('cart/delete/<int:cart_id>', views.delete_from_cart, name='cartDelete'),
    path('cart/increment/<int:cart_id>', views.increment_cart_item, name='cartIncrement'),
    path('cart/decrement/<int:cart_id>', views.decrement_cart_item, name='cartDecrement'),

    path('<int:product_id>/shop-single.html', views.shop_single, name='shopSingle'),
]