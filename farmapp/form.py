from .models import Post,Business, Image
from django.forms import fields
from django import forms


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'price']

class BusinessForms(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Business
        fields= ['name','email','business_image','location']

class PostForms(forms.ModelForm):
    class Post:
        fields=['post']


from django import forms
from .models import Product

# class AddProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['product_name', 'product_quantity', 'product_price']