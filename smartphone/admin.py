from django.contrib import admin
from .models import SmartPhone,SmartPhoneBrand,Memory
# Register your models here.

admin.site.register(SmartPhoneBrand)
admin.site.register(SmartPhone)
admin.site.register(Memory)
