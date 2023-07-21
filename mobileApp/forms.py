from django import forms
from .models import Category, Product, Order

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productName', 'description', 'price', 'categoryName']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderDate', 'productName', 'orderTime', 'seller']
