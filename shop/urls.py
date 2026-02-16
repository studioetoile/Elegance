from django.urls import path
from .views import home, add_product_to_cart, view_cart, contact, remove_product_from_cart

from . import views



urlpatterns = [
    path("", home, name="home"),
    path("add-to-cart/<int:product_id>/", add_product_to_cart, name="add_to_cart"),
]

from .views import view_cart
from .views import home, add_product_to_cart, view_cart, contact, remove_from_cart


urlpatterns = [
    path("", home, name="home"),
    path("add-to-cart/<int:product_id>/", add_product_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="view_cart"),  # ← nouvelle URL
    path("contact/", contact, name="contact"),
    path("remove-from-cart/<int:product_id>/", remove_product_from_cart, name="remove_from_cart"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # tes autres urls...
    path("category/<int:category_id>/", views.products_by_category, name="products_by_category"),
    path("search/", views.search, name="search"),
    path("products/", views.all_products, name="all_products"),

]

#si j'ajoute un url path ici, je dois ajouter cette nouvelle vue dans view.py
