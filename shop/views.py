from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .cart import add_to_cart

# shop/views.py
from django.shortcuts import render, redirect
from .models import Product, Category 
from .cart import add_to_cart as cart_add, remove_from_cart as cart_remove

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {"products": products,"categories":categories})

def view_cart(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for product_id_str, quantity in cart.items():
        product = Product.objects.get(id=int(product_id_str))
        cart_items.append({"product": product, "quantity": quantity})
        total += product.price * quantity

    return render(request, "cart.html", {"cart_items": cart_items, "total": total})

def add_product_to_cart(request, product_id):
    cart_add(request, product_id)
    return redirect("view_cart")

def remove_product_from_cart(request, product_id):
    cart_remove(request, product_id)
    return redirect("view_cart")


def contact(request):
    return render(request, "shop/contact.html")



def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            del cart[product_id_str]

    request.session['cart'] = cart
    return redirect('view_cart')



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    parent = product.parent_product if product.parent_product else product
    color_variants = parent.variants.exclude(id=product.id)

    # related product a été ajouté pour "cela pourrait vous intéresser"
    related_products = Product.objects.filter(
        category=product.category
    ).exclude(id=product.id)[:4]  # max 4 produits

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'color_variants': color_variants,
        "related_products":related_products,
    })


#Pour que quand je clique sur une catégorie, les produits de celle ci s'affiche
def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    print("CATÉGORIE :", category.name)
    print("NB PRODUITS :", products.count())


    categories = Category.objects.all()

    return render(request, "shop/products_by_category.html", {
        "category": category,
        "products": products,
        "categories": categories,
    })

from django.db.models import Q

def search(request):
    query = request.GET.get("q")
    products = []

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, "shop/search_results.html", {
        "products": products,
        "query": query
    })

from .models import Product, Category

def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "shop/all_products.html", {
        "products": products,
        "categories": categories,
    })