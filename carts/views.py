from django.shortcuts import render , redirect
from store.models import Product
from .models import Cart , CartItem
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    # print("Session Key" , cart)
    if not cart:
        request.session.create()
        cart = request.session.session_key
        # print("Generated Session key" , cart)
    return cart

def add_cart(request , product_id):
    product = Product.objects.get(id=product_id)
    # print("Product fetched by ID" , product)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart) # argument me left side wala models ka field hai aur right side wala product object hai jo uper liya gya hai.
        cart_item.quantity += 1
        cart_item.save()
    
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart')

def cart(request , total = 0, quantity = 0, cart_items = None):
    try: 
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart , is_active = True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (2 * total) / 100
        grand_total = tax + total
    
    except Cart.DoesNotExist:
        print("Except block running")

    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total
    }
    return render(request , "store/cart.html" , context)