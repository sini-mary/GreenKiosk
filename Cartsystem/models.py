from django.db import models
from inventory.models import Product
from  Order.models import Order

# Create your models here.
class Cart(models.Model):
    products = models.OneToOneField(Product,on_delete=models.CASCADE,null=True)
    orderrr =  models.OneToOneField(Order,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="images")
    total = models.IntegerField()
    number_of_products = models.IntegerField()
    shipping_cost = models.FloatField()
    Payment_options = models.TextField()
    discounts = models.FloatField()
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return  self.product
