from django.shortcuts import render
from .models import Category
# Create your views here.
def getAllCategory(request):
    categories = Category.objects.all()
    return dict(categories = categories)
