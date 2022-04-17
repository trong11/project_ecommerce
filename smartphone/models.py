from django.db import models

# Create your models here.
class SmartPhoneBrand(models.Model):
    br_name  = models.CharField(max_length=200, unique=True)
    br_phonenumber = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.br_name

class Memory(models.Model):
    size = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.size


class SmartPhone(models.Model):
    phone_name  = models.CharField(max_length=200, unique=True)
    import_price = models.IntegerField()
    memory = models.ForeignKey(Memory,on_delete = models.CASCADE)
    manufacturing_date = models.DateField()
    smartphonebrand = models.ForeignKey(SmartPhoneBrand,on_delete = models.CASCADE)

    def __str__(self):
        return self.phone_name
