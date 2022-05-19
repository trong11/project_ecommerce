from django.contrib import admin

from customer.models import Customer, CustomerAccount, CustomerAddress, FullName

# Register your models here.
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('username','email')
admin.site.register(CustomerAccount)
admin.site.register(CustomerAddress)
admin.site.register(FullName)
admin.site.register(Customer)
