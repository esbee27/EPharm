from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass

class Product(models.Model):
    seller = models.ForeignKey(CustomUser)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='customer/product_images/')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product)
    id = models.IntegerField(max_length=255)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='customer/product_images/')

    def __str__(self):
        return self.product