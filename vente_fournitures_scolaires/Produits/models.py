from django.db import models

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='produits/')

    def __str__(self):
        return self.nom



