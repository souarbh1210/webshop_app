from django.shortcuts import render

from shop.models import Product
from django.db.models import Q
def servicesResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products= Product.objects.all().filter(Q(name__contain=query)| Q(decription__contain=query))
        #description ki spell galat h
    return render(request,'services.html',{'query':query,'products':products})