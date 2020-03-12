from django.db import models
from django.utils.translation import gettext_lazy as _


# product category
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# product brand
class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


# product
class Product(models.Model):

    class Status(models.TextChoices):
        PENDING = 'Pending', _('PENDING')
        PUBLISHED = 'Published', _('PUBLISHED')
        STOCK_OUT = 'Stock Out', _('STOCK_OUT')

    name = models.CharField(max_length=100)
    slug = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.png', null=True, blank=True, upload_to='product_images')
    description = models.TextField(max_length=100)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


# filtering
class QueryStrings(models.Model):
    data = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.data


