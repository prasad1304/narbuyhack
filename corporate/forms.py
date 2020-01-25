from django import forms
from django.contrib.auth.models import User
from .models import Corporate, ContactModel, Items, CorperateGroup


class CorporateLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Corporate
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username', 'email']


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['shop_name', 'city', 'district', 'password',
                  'area', 'email']


class FarmerForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ['item_name', 'item_quantity','price','product_description','image'
                  
                  ]


