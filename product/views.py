from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Brand, Product


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'

