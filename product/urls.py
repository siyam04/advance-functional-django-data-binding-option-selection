from django.urls import path

from .views import products, search


app_name = 'product'

urlpatterns = [

    # CBV
    # path('product-list', ProductList.as_view(), name='product-list'),

    # FBV
    path('', products, name='products'),

    path('<int:query_id>', products, name='products_query_id'),

    path('search', search, name='search'),

]
