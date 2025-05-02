from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .models import Cart, CartItem
from .forms import CartAddProductForm

def cart_detail(request):
    cart = request.cart  # We'll set this in middleware or context processor
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def cart_add(request, product_id):
    cart = request.cart
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': cd['quantity'], 'price': product.price}
        )
        if not created:
            item.quantity += cd['quantity']
            item.save()
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = request.cart
    product = get_object_or_404(Product, id=product_id)
    cart.items.filter(product=product).delete()
    return redirect('cart:cart_detail')