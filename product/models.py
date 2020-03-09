from django.db import models


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

    STATUS = (
        ('Pending', 'PENDING'),
        ('Published', 'PUBLISHED'),
        ('Stock Out', 'STOCK OUT')
    )

    name = models.CharField(max_length=100)
    slug = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.png', null=True, blank=True, upload_to='product_images')
    description = models.TextField(max_length=100)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
