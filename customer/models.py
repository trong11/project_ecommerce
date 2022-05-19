from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class FullName(models.Model):
    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name

class CustomerAccount(models.Model):
    username      = models.CharField(max_length=50,unique=True)
    password      = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class CustomerAddress (models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=50)

    def __str__(self):
        return self.city

    
class Customer (models.Model):
    fullname = models.ForeignKey(FullName,on_delete=models.CASCADE)
    customer_account = models.ForeignKey(CustomerAccount,on_delete=models.CASCADE)   
    customer_address = models.ForeignKey(CustomerAddress,on_delete=models.CASCADE)  
    email         = models.EmailField(max_length=100,unique=True)
    phone_number  = models.CharField(max_length=50)
    

    
    def __str__(self):
        return self.email       