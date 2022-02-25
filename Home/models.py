from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    price = models.IntegerField()
    img = models.ImageField(upload_to='product_images', max_length=100)
