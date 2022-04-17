from django.contrib import admin
from .models import Clothes,ClothesCategory,ClothesBrand
# Register your models here.


admin.site.register(ClothesCategory)
admin.site.register(ClothesBrand)
admin.site.register(Clothes)
