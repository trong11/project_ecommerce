from django.shortcuts import render
from shop.models import Item


def home(request):
    items = Item.objects.all().filter(is_available__in = [True])

    context = {
        'items' : items,
    }

    return render(request,'home.html', context)
