from django.shortcuts import render
from .models import Product
def product_list(request):
    return render(request,"gallery/index.html",{"products":Product.objects.all()})
