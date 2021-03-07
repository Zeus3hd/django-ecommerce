from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    #https://en.wikipedia.org/wiki/Database_index
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)
    
    # class Meta is optional additional data that are not fields
    class Meta:
        verbose_name_plural = 'categories'
    
    # to reference data by name
    def __str__(self):
        return self.name


class Product(models.Model):
    # associate categories to the product, on_delete: deleting all products under that category
    category = models.ForeignKey(Category,related_name="product",on_delete=models.CASCADE)
    # associate product to user, on_delete all products for user
    created_by = models.ForeignKey(User, related_name="product_creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # author of the book not the one that created the Product/Entry
    author = models.CharField(max_length=255,default="admin")
    description = models.TextField(blank=True)
    # we're not storing the image in the database, but storing the link to the image
    image = models.ImageField(upload_to="images/")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        # the - is for descending order
        ordering = ('-created',)