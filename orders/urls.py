from django.urls import path
from . import views

urlpatterns = [
   path('add_order',views.addOrder,name = 'add_order'),
   path('payment',views.payment,name = 'payment'),

]
