from django.contrib import admin
from .models import Product

#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
 #   list_display = ('name', 'price', 'stock')
 #   search_fields = ('name', 'description')


from django.contrib import admin
from .models import Product, ProductImage, Category
from django.utils.html import format_html

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1



#@admin.register(Product)
admin.site.register(Category)
admin.site.register(Product)

# Admin pour le modèle Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', "descriptiondetaillee","parent_product", "color","color_preview","category")  # Colonnes affichées dans l'admin
    #list_display = ('name', 'price', 'stock', "color")
    list_filter = ('price',)                   # Filtres sur la droite
    search_fields = ('name', 'description')   # Barre de recherche
    ordering = ('name',)                       # Tri par défaut
    list_editable = ('stock',)                 # Permet de modifier le stock directement
    inlines = [ProductImageInline]
    def color_preview(self, obj):
        if not obj.color:
            return "-"
        return format_html(
            '<span class="color-box {}"></span>',
            obj.color
        )
   
    color_preview.short_description = "Couleur"

# Enregistrement du modèle avec son admin
#admin.site.register(Product, ProductAdmin)

