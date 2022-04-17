from django.contrib import admin
from .models import Laptop,LaptopRAM,LaptopBrand
# Register your models here.

admin.site.register(LaptopRAM)
admin.site.register(LaptopBrand)
admin.site.register(Laptop)
