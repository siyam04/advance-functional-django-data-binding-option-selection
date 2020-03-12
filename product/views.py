from urllib import parse
from urllib.parse import urlencode
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Category,
    Brand,
    Product,
    QueryStrings
)


# CBV
# class ProductList(ListView):
#     model = Product
#     template_name = 'product_list.html'


# FBV
def products(request, query_id=None):
    products = Product.objects
    # print(products)
    # print(type(products))

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

    template = 'product_list.html'

    return render(request, template, context)


# submitted selection data
def search(request):
    print(request.POST)

    fields_data = search_form_fields_filter(request.POST)
    query_id = store_querystring(fields_data)

    return redirect('product:products_query_id', query_id)


# returns list of custom field names
def search_form_fields():
    return ['brand', 'category', 'status']


def search_form_fields_filter(query_dict):
    # print('TEST:', query_dict)
    query_string = {}

    for i in search_form_fields():
        if query_dict.get(i):
            query_string.update({i: query_dict.get(i)})

    return query_string


def store_querystring(data):
    query_data = QueryStrings.objects.create(data=urlencode(data))
    # print(query_data)
    # print(query_data.id)
    return query_data.id


def process_query_string(query_id):
    query_string = QueryStrings.objects.get(pk=query_id)
    return dict(parse.parse_qsl(query_string.data))


