# carts/context_processors.py

from .models import Cart, CartItem

def counter(request):
    quantity = 0

    try:
        cart = Cart.objects.get(cart_id=request.session.session_key)
        cart_items = CartItem.objects.filter(cart=cart)

        for item in cart_items:
            quantity += item.quantity
    except:
        pass

    return {
        'quantity': quantity
    }