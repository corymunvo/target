from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from phonenumber_field.formfields import PhoneNumberField


class SignUpForm(UserCreationForm):
    first_name  = forms.CharField(label='First Name', max_length=100)
    last_name  = forms.CharField(label='Last Name', max_length=100)
    company  = forms.CharField(label='Company', max_length=100)
    address_line_one  = forms.CharField(label='Adress', max_length=200)
    address_line_two  = forms.CharField(max_length=200)
    phone  = PhoneNumberField()
    country  = CountryField(blank_label='(Select country)').formfield()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'company', 'address_line_one', 'address_line_two', 'phone', 'country' )
        widgets = {'country': CountrySelectWidget()}