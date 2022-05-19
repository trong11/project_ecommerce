from django.db import models
from category.models import Category
from book.models import Book
from clothes.models import Clothes
from laptop.models import Laptop
from smartphone.models import SmartPhone
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=200,unique=True)
    description  = models.TextField(max_length=500, blank=True)
    price        = models.IntegerField()
    images       = models.ImageField(upload_to='photos/products')
    stock        = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category     = models.ForeignKey(Category,on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    modified_date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name

    def get_url(self):
        return reverse('item_detail',args=[self.category.slug, self.slug])

    def get_item_book(self):
        return BookItem.objects.get(id = self.id)

    def get_item_clothes(self):
        return ClothesItem.objects.get(id = self.id)

    def get_item_laptop(self):
        return LaptopItem.objects.get(id = self.id)

    def get_item_smartphone(self):
        return SmartPhoneItem.objects.get(id = self.id)


class BookItem(Item):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)

class ClothesItem(Item):
    clothes = models.ForeignKey(Clothes,on_delete = models.CASCADE)
    clothes_size = models.IntegerField()

class LaptopItem(Item):
    laptop = models.ForeignKey(Laptop,on_delete = models.CASCADE)
    weight = models.IntegerField()
    width = models.IntegerField()

class SmartPhoneItem(Item):
    smartphone = models.ForeignKey(SmartPhone,on_delete = models.CASCADE)
    weight = models.IntegerField()
    width = models.IntegerField()
    color = models.CharField(max_length=200)
