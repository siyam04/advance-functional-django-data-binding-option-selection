from urllib import parse

from django.contrib import messages
from urllib.parse import urlencode
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .models import Category, Brand, Product, QueryStrings


# CBV
# class ProductList(ListView):
#     model = Product
#     template_name = 'product_list.html'


# FBV
def products(request, template='product_list.html', query_id=None):
    # print(query_id)
    products = Product.objects

    if query_id:
        query_dict = process_query_string(query_id)
        products = products.filter(**query_dict)

    products =  products.all()
    brands = Brand.objects.filter()
    categories = Category.objects.filter()
    statuses = Product.Status.choices

    context = {
        'products': products,
        'brands': brands,
        'categories': categories,
        'statuses': statuses
    }

    return render(request, template, context)


def search(request):
    fields_data = search_form_fields_filter(request.POST)
    query_id = store_querystring(fields_data)

    return redirect('product:products_query_id', query_id)


def search_form_fields():
    return ['brand', 'category', 'status']


def search_form_fields_filter(query_dict):
    query_string = {}
    for i in search_form_fields():
        if query_dict.get(i):
            query_string.update({i: query_dict.get(i)})

    return query_string


def store_querystring(data):
    query_data = QueryStrings.objects.create(data=urlencode(data))
    return query_data.id


def process_query_string(query_id):
    query_string = QueryStrings.objects.get(pk=query_id)
    return dict(parse.parse_qsl(query_string.data))
