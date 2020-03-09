from django.contrib import admin
from django.utils.html import format_html

from .models import (

    Category,
    Brand,
    Product,

)

# 'Group' class hiding from the superuser

# from django.contrib.auth.models import Group

# admin.site.unregister(Group)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    # filter_horizontal = ['staff']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description', 'price', 'status', 'category', 'brand', 'image']
    list_display_links = ['name']
    list_filter = ['name', 'status']
    search_fields = ['name', 'status', 'category']


# Registering databases
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)


