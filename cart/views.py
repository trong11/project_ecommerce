from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def _getCartID(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def addToCart(request,item_id):
    item = Item.objects.get(id=item_id)
    try:
        cart = Cart.objects.get (cart_id = _getCartID(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
             cart_id = _getCartID(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(item=item, cart=cart)
        cart_item.quantity += 1
        current_user = request.user
        cart_item.user = current_user
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
           item = item,
           quantity = 1,
           cart = cart
        )
        cart_item.save()
    return redirect('cart')

@login_required(login_url='login')
def getCartItem(request,total=0,quantity=0,cart_items=None):
    try:
        tax = 0
        totalAmount = 0
        cart = Cart.objects.get(cart_id = _getCartID(request))
        cart_items = CartItem.objects.filter(cart = cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.item.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        totalAmount = total + tax + 50000
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'totalAmount':totalAmount,
    }
    return render(request,'shop/cart.html',context)

def minusCartItem(request,item_id):
    cart = Cart.objects.get(cart_id = _getCartID(request))
    item = get_object_or_404(Item,id=item_id)
    cart_item = CartItem.objects.get(item = item,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def deleteCartItem(request,item_id):
    cart = Cart.objects.get(cart_id = _getCartID(request))
    item = get_object_or_404(Item,id = item_id)
    cart_item = CartItem.objects.get(item = item,cart=cart)
    cart_item.delete()
    return redirect('cart')


@login_required(login_url='login')
def checkoutCartItem(request,total=0,quantity=0,cart_items=None):
    try:
        tax = 0
        totalAmount = 0
        cart = Cart.objects.get(cart_id = _getCartID(request))
        cart_items = CartItem.objects.filter(cart = cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.item.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        totalAmount = total + tax + 50000
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'totalAmount':totalAmount,
    }
    return render(request,'shop/checkout.html',context)