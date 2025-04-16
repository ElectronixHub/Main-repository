# from django.http import HttpResponse
# return HttpResponse("Welcome to the homepage of my Django project!")

# def main(request):
#     return HttpResponse()

from django.shortcuts import render
from django.shortcuts import redirect


def homepage(request):
    return render(request, 'Index.html')

def redirect_to_home(request):
    return redirect(request, 'Index.html')

def signin(request):
    return render(request, 'signin.html')


def devices(request):
    return render(request, 'devices.html')

def cart(request):
    return render(request, 'cart.html')

def laptops(request):
    return render(request, 'Laptops.html')


def mobiles(request):
    return render(request, 'mobiles.html')


def screens(request):
    return render(request, 'screens.html')

def tablets(request):
    return render(request, 'tablets.html')











# from django.shortcuts import get_object_or_404, redirect, render
# from .models import Product, Cart, CartItem

# def add_to_cart(request, product_id):
    # Get the product
    # product = get_object_or_404(Product, id=product_id)

    # Get or create a cart for the session
    # cart_id = request.session.get('cart_id')
    # if cart_id:
    #     cart = Cart.objects.get(id=cart_id)
    # else:
    #     cart = Cart.objects.create()
    #     request.session['cart_id'] = cart.id

    # Add the product to the cart
    # cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    # if not created:
    #     cart_item.quantity += 1
    #     cart_item.save()

    # return redirect('/cart/')  # Redirect to the cart page










# def cart(request):
#     cart_id = request.session.get('cart_id')
#     if cart_id:
#         cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
#     else:
#         cart = None

#     return render(request, 'cart.html', {'cart': cart})











