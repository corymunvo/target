import csv
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import  ProfileForm, CartForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from decimal import *
from .models import Product, Cart
from django.db import transaction

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def paginate_products(request, sort):
    product_list = Product.objects.all().order_by(sort)
    paginator = Paginator(product_list, 6)  # Show 6
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {'products': products}
    return context

def get_user_cart(user):
    cart = Cart.objects.filter(user=user).select_related()
    subtotal = 0
    for item in cart:
        subtotal += item.quantity * item.product.price

    total = str(round(subtotal * Decimal(1.12), 2))
    context = {'cart': cart, 'subtotal': subtotal, 'total': total }
    return context

def clear_cart(user):
    cart = Cart.objects.filter(user=user).delete()
    

def index(request):
    context = paginate_products(request, 'id')
    return render(request, 'fashion/index.html', context)


def about(request):
    return render(request, 'fashion/about.html')


def catalogue(request):
    context = paginate_products(request, 'category')
    return render(request, 'fashion/catalogue.html', context)


def delete_from_cart(request, cart_id):
    Cart.objects.filter(pk=cart_id, user=request.user).delete()
    return redirect('cart')

def increment_cart_item(request, cart_id):
    cart_item = Cart.objects.filter(pk=cart_id, user=request.user).first()
    cart_item.quantity = clamp(cart_item.quantity + 1, 1,100)
    cart_item.save()
    return redirect('cart')

def decrement_cart_item(request, cart_id):
    cart_item = Cart.objects.filter(pk=cart_id, user=request.user).first()
    cart_item.quantity = clamp(cart_item.quantity - 1, 1,100)
    cart_item.save()
    
    return redirect('cart')

@login_required
def cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            cart = form.save(commit=False)
            new_cart, created = Cart.objects.get_or_create(user=request.user, product=cart.product)
            new_cart.quantity = clamp(form.cleaned_data.get('quantity'), 1,100)
            new_cart.save()
    
    context = get_user_cart(request.user)
    return render(request, 'fashion/cart.html', context)

@login_required
def checkout(request):
    context = get_user_cart(request.user)
    return render(request, 'fashion/checkout.html', context)

@login_required
def thank_you(request):
    clear_cart(request.user)
    return render(request, 'fashion/thankyou.html')



def contact(request):
    return render(request, 'fashion/contact.html')


def shop(request):
    context = paginate_products(request, 'message')
    return render(request, 'fashion/shop.html', context)


def arrivals(request):
    context = paginate_products(request, 'updated_at')
    return render(request, 'fashion/arrivals.html', context)


@transaction.atomic
def sign_up(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')    

    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'fashion/sign-up.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def shop_single(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = CartForm({'product': product_id})
    return render(request, 'fashion/shop-single.html', {'product': product, 'form': form})


def csv_products(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    product_list = Product.objects.all().order_by('id')
    t = loader.get_template('fashion/product.txt')
    c = {'data': product_list}
    response.write(t.render(c))


    return response