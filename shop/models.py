from django.db import models


#class Product(models.Model):
 #   name = models.CharField(max_length=200)
  #  price = models.DecimalField(max_digits=8, decimal_places=2)
   # stock = models.IntegerField()
#    description = models.TextField()
#    image = models.ImageField(upload_to='products/', blank=True, null=True)  # ← Nouvelle ligne

#    def __str__(self):
#        return self.name

# shop/models.py



#Catégorie 

class Category(models.Model):
    name = models.CharField(max_length=100)
    #slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    descriptiondetaillee = models.TextField(blank=True, verbose_name="Description détaillée")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)  # ← nouveau champ

    color = models.CharField(max_length=50, null=True, blank=True)
    parent_product = models.ForeignKey('self', null=True, blank=True, related_name='variants', on_delete=models.SET_NULL)
    
    COLOR_CHOICES = [
        ("red", "Rouge"),
        ("blue", "Bleu"),
        ("green", "Vert"),
        ("black", "Noir"),
        ("white", "Blanc"),
    ]

    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products",null=True, blank=True)

    is_parent = models.BooleanField(default=True)

    def __str__(self):
        #return f"{self.name} ({self.color})" if self.color else self.name
        return self.name


#INSÉRER UNE GALERIE DE PHOTO PAR L'ADMIN POUR CHAQUE PRODUIT
class ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"Image de {self.product.name}"

