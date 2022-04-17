from django.db import models

# Create your models here.
class ClothesCategory(models.Model):
    cate_name  = models.CharField(max_length=200, unique=True)
    cate_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.cate_name


class ClothesBrand(models.Model):
    br_name  = models.CharField(max_length=200, unique=True)
    br_phonenumber = models.CharField(max_length=200, unique=True)
    br_address = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.br_name

class Clothes(models.Model):
    clothes_name  = models.CharField(max_length=200, unique=True)
    import_price = models.IntegerField()
    clothes_description = models.TextField(max_length=500, blank=True)
    clothescategory = models.ForeignKey(ClothesCategory,on_delete = models.CASCADE)
    clothesbrand = models.ForeignKey(ClothesBrand,on_delete = models.CASCADE)

    def __str__(self):
        return self.clothes_name
