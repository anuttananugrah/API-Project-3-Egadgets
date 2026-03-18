from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    options=(
        ("Smartphone","Smartphone"),
        ("Tablets","Tablets"),
        ("Smartwatch","Smartwatch")
    )
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    image=models.ImageField(upload_to="product_image")
    price=models.PositiveIntegerField()
    category=models.CharField(max_length=100,choices=options)

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100)
    
class Review(models.Model):
    review=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)