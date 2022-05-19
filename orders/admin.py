from django.contrib import admin

from orders.models import Order, Payment, Shipment

# Register your models here.
admin.site.register(Payment)
admin.site.register(Shipment)
admin.site.register(Order)