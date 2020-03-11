from django.urls import path, include

from .views import products, search


app_name = 'product'

urlpatterns = [

    # all products CBV
    # path('product-list', ProductList.as_view(), name='product-list'),

    # all products FBV
    path('', products, name='products'),

    path('<int:query_id>', products, name='products_query_id'),

    path('search', search, name='search'),

]
