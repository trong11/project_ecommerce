from django.urls import path
from . import views
urlpatterns = [
     path ('',views.getCartItem,name = 'cart'),
     path('add_to_cart/<int:item_id>/',views.addToCart,name='add_to_cart'),
     path('minus_cart/<int:item_id>/',views.minusCartItem,name='minus_cart'),
     path('delete_cart_item/<int:item_id>/',views.deleteCartItem,name='delete_cart_item'),
     path('checkout/',views.checkoutCartItem,name='checkout'),
]
