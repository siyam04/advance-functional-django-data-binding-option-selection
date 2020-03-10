from django.urls import path, include

from .views import ProductList


app_name = 'product'

urlpatterns = [

    # all products
    path('product-list', ProductList.as_view(), name='product-list'),

]
