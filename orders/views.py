import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from cart.models import CartItem
from orders.models import Order, Shipment,Payment

# Create your views here.
def addOrder(request,total=0,quantity=0):
    current_user = request.user

    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    
    if(cart_count<=0):
        return redirect('shop')

    grand_total = 0
    tax = 0 

    for cart_item in cart_items:
        total += (cart_item.item.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2*total)/100
    total_amount = total + tax +50000    



    if request.method == 'POST':
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        note = request.POST['order_note']

        shipment = Shipment.objects.create (shipping_cost = 50000,address = address,city=city,country=country)
        shipment.save()

        customer = current_user.get_customer()

        order = Order.objects.create (customer = customer,shipment = shipment,order_total_amount = total_amount,note = note,tax=tax) 
        order.save()

        context = {
           'order': order,
           'cart_items': cart_items,
           'total': total,
           'tax': tax,
           'total_amount':total_amount,
        }

        return render(request,'orders/payment.html',context)
    else:
        return redirect ('checkout')    


def payment(request):
    body = json.loads(request.body)
    current_user = request.user
    order = Order.objects.get(id=body['orderID'])

    payment = Payment (
          customer = current_user.get_customer(),
          payment_id = body['transID'],
          payment_method = body['payment_method'],
          total_amount = order.order_total_amount,
    )
    payment.save()
    order.payment=payment
    order.save()
    return render(request,'orders/payment.html')

