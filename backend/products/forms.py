from django import forms
from .models import Product

class ProductForm(forms.ModelForms):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price'
        ]