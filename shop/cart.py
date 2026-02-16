# shop/cart.py
from .models import Product

def add_to_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session["cart"] = cart

def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            del cart[product_id_str]

    request.session["cart"] = cart

def add(self, product, color):
    self.cart[str(product.id)] = {
        "name": product.name,
        "price": str(product.price),
        "color": color,
        
    }

#product.color
