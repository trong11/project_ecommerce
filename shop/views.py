from django.shortcuts import render,get_object_or_404
from .models import Item
from category.models import Category
from cart.views import _getCartID
from cart.models import *
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.http import HttpResponse

# Create your views here.
def getItem(request):
    items = Item.objects.all().filter(is_available__in = [True])
    paginator = Paginator(items,8)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)

    context = {
        'items' : paged_items,
    }
    return render(request,'shop/shop.html',context)

def getItemByCategory(request,category_slug):
    categories = get_object_or_404 (Category,slug = category_slug)
    items = Item.objects.filter(category=categories,is_available=True)
    paginator = Paginator(items,8)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)

    context = {
        'items' : paged_items,
    }
    return render(request,'shop/shop.html',context)

def getItemDetail(request,category_slug,item_slug):
    try:
        single_item = Item.objects.get(category__slug=category_slug,slug=item_slug)
        check_cart = CartItem.objects.filter(cart__cart_id=_getCartID(request),item = single_item).exists()

    except Exception as e:
        raise e

    context = {
       'single_item' : single_item,
       'check_cart':check_cart
    }
    return render(request,'shop/item_detail.html',context)


def getItemByName(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            items = Item.objects.order_by('-created_date').filter(item_name__icontains=keyword)
    context = {
        'items' : items,
    }
    return render(request,'shop/shop.html',context)
