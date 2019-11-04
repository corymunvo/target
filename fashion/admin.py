from django.contrib import admin

# Register your models here.
from .models import Product, Profile

class ProductAdmin(admin.ModelAdmin):
    fields = ['label', 'image_url', 'price', 'stars']
    list_display = ('label', 'image_url', 'price', 'stars')

admin.site.register(Product,  ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'country']
    list_display = ('first_name', 'last_name', 'country')

admin.site.register(Profile,  ProfileAdmin)


