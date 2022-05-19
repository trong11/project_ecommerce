from django.db import models
from accounts.models import Account
from shop.models import Item
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length = 250,blank = True)
    cart_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    item = models.ForeignKey(Item ,on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart ,on_delete = models.CASCADE)
    user = models.ForeignKey(Account ,on_delete = models.CASCADE,null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.item.item_name

    def countTotal(self):
        return self.item.price * self.quantity    


