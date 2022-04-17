from django.db import models

# Create your models here.
class LaptopBrand(models.Model):
    br_name  = models.CharField(max_length=200, unique=True)
    br_phonenumber = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.br_name

class LaptopRAM(models.Model):
    ram_name  = models.CharField(max_length=200, unique=True)
    memory = models.IntegerField()

    def __str__(self):
        return self.ram_name


class Laptop(models.Model):
    lap_name  = models.CharField(max_length=200, unique=True)
    import_price = models.IntegerField()
    chip = models.CharField(max_length=200, unique=True)
    manufacturing_date = models.DateField()
    laptopram = models.ForeignKey(LaptopRAM,on_delete = models.CASCADE)
    laptopbrand = models.ForeignKey(LaptopBrand,on_delete = models.CASCADE)

    def __str__(self):
        return self.lap_name
