from django.db import models

# Create your models here.
class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)

class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderDate = models.DateField()
class Order1(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderDate = models.DateField()

