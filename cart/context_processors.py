#this file is used to make a class global

from .cart import Cart

def cart(request):
    return {'cart':Cart(request)}