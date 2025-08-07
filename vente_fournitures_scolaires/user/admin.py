from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profil, Client, Vendeur, Contact

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'adresse', 'telephone')
    search_fields = ('user__username', 'adresse', 'telephone')

@admin.register(Vendeur)
class VendeurAdmin(admin.ModelAdmin):
    list_display = ('user', 'nom_entreprise', 'numero_siret')
    search_fields = ('user__username', 'nom_entreprise', 'numero_siret')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date_soumission')
    search_fields = ('nom', 'email')
    readonly_fields = ('date_soumission',)
