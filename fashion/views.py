import csv
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from .models import Product


def paginate_products(request):
    product_list = Product.objects.all().order_by('id')
    paginator = Paginator(product_list, 6)  # Show 6
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {'products': products}
    return context


def index(request):
    context = paginate_products(request)
    return render(request, 'fashion/index.html', context)


def about(request):
    return render(request, 'fashion/about.html')


def catalogue(request):
    context = paginate_products(request)
    return render(request, 'fashion/catalogue.html', context)


def cart(request):
    return render(request, 'fashion/cart.html')


def checkout(request):
    form = SignUpForm()
    return render(request, 'fashion/checkout.html', {'form': form})


def contact(request):
    return render(request, 'fashion/contact.html')


def shop(request):
    context = paginate_products(request)
    return render(request, 'fashion/shop.html', context)


def arrivals(request):
    context = paginate_products(request)
    return render(request, 'fashion/arrivals.html', context)


def thankyou(request):
    return render(request, 'fashion/thankyou.html')


def signUp(request):
    if request.method == 'POST':
        print("post")
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.company = form.cleaned_data.get('company')
            user.profile.address_line_one = form.cleaned_data.get('address_line_one')
            user.profile.address_line_two = form.cleaned_data.get('address_line_two')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.country = form.cleaned_data.get('country')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'fashion/sign-up.html', {'form': form})


def shopSingle(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'fashion/shop-single.html', {'product': product})


def csvProducts(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    product_list = Product.objects.all().order_by('id')

    writer = csv.writer(response)

    for product in product_list:
        writer.writerow([product.id, product.label, '', '', product.image_url, product.price, '', 100, product.price, '', '', '', '', '', '', '', '', '', '', '', ''])

    return response