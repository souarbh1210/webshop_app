from django.shortcuts import render,redirect
from shop.models import Product
from .models import Cart,CartItem
from django.core.exceptions import  ObjectDoesNotExist
def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_cart(request,product_id):
     product=Product.objectsget(id=product_id)
     try:
         cart = Cart.objects.get(card_id=cart_id(request))
     except Cart.DoesNotExist:
         cart = Cart.object.create(
             card_id=cart_id(request)
         )
         cart.save()
     try:
         cart_item = CartItem.objects.get(product=product,cart= cart)
         cart_item.quantity +=1
         cart_item.save()
     except CartItem.DoesNotExist:
                               pass


