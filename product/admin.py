from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import (

    Category,
    Brand,
    Product,
    QueryStrings
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


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    # filter_horizontal = ['staff']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description', 'price', 'status', 'category', 'brand', 'image']
    list_display_links = ['name']
    list_filter = ['name', 'status']
    search_fields = ['name', 'status', 'category']

    # readonly_fields = ['image']
    #
    # def image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url=obj.image.url,
    #         width=obj.image.width,
    #         height=obj.image.height,
    #     )
    # )


@admin.register(QueryStrings)
class QueryStringsAdmin(admin.ModelAdmin):
    list_display = ['id', 'data']



# Registering databases
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Brand, BrandAdmin)
# admin.site.register(QueryStrings)


