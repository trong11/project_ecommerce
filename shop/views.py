from django.shortcuts import render,get_object_or_404
from .models import Item
from category.models import Category

# Create your views here.
def getItem(request):
    items = Item.objects.all().filter(is_available__in = [True])

    context = {
        'items' : items,
    }
    return render(request,'shop/shop.html',context)

def getItemByCategory(request,category_slug):
    categories = get_object_or_404 (Category,slug = category_slug)
    items = Item.objects.filter(category=categories,is_available=True)

    context = {
        'items' : items,
    }
    return render(request,'shop/shop.html',context)

def getItemDetail(request,category_slug,item_slug):
    try:
        single_item = Item.objects.get(category__slug=category_slug,slug=item_slug)
    except Exception as e:
        raise e

    context = {
       'single_item' : single_item,
    }
    return render(request,'shop/item_detail.html',context)
