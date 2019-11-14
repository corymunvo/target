from django.contrib import admin

# Register your models here.
from .models import Product, Profile, Cart

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'thumbnail_url', 'price', 'stars']
    list_display = ('name', 'thumbnail_url', 'price', 'stars')

admin.site.register(Product,  ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'country']
    list_display = ('first_name', 'last_name', 'country')

admin.site.register(Profile,  ProfileAdmin)


class CartAdmin(admin.ModelAdmin):
    fields = ['quantity', 'product', 'user']
    list_display = ('quantity', 'product', 'user')

admin.site.register(Cart,  CartAdmin)
