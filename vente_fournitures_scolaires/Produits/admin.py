from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Produit

class ProduitAdmin(admin.ModelAdmin):
    # Configuration de l'affichage dans la liste des produits
    list_display = ('nom', 'prix', 'image_preview')
    list_filter = ('prix',)
    search_fields = ('nom', 'description')
    ordering = ('nom',)
    readonly_fields = ('image_preview',)
    
    # Pour afficher un aperçu de l'image dans l'admin
    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url))
        return "Aucune image"
    
    image_preview.short_description = 'Aperçu'

# Enregistrement du modèle avec sa classe d'administration
admin.site.register(Produit, ProduitAdmin)