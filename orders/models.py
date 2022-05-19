from ast import Or
from operator import mod
from django.db import models
from customer.models import Customer
from shop.models import Item


# Create your models here.
class Payment (models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

class Shipment(models.Model):
    shipping_cost = models.IntegerField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    shipment = models.ForeignKey(Shipment,on_delete=models.SET_NULL,blank=True,null=True)
    order_total_amount = models.FloatField()
    note = models.CharField(max_length=100,blank=True)
    tax = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.customer.fullname.first_name + self.customer.fullname.last_name
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)  
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)  
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.item_name

