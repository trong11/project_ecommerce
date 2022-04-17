from django.contrib import admin
from .models import Item,BookItem,ClothesItem,LaptopItem,SmartPhoneItem,Color

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('item_name',)}
    list_display = ('item_name','price','stock','category','modified_date','is_available')


admin.site.register(Item,ProductAdmin)
admin.site.register(BookItem,ProductAdmin)
admin.site.register(ClothesItem,ProductAdmin)
admin.site.register(LaptopItem,ProductAdmin)
admin.site.register(SmartPhoneItem,ProductAdmin)
admin.site.register(Color)
