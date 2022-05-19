from django.urls import path
from . import views
urlpatterns = [
    path('',views.getItem,name='shop'),
    path('category/<slug:category_slug>/',views.getItemByCategory,name='item_by_category'),
    path('category/<slug:category_slug>/<slug:item_slug>/',views.getItemDetail,name='item_detail'),
    path('search/',views.getItemByName,name = 'search'),
]
