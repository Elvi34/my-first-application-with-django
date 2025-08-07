# users/models.py
from django.db import models
from django.contrib.auth.models import User

# Définir les choix de rôles pour plus de clarté
ROLE_CHOICES = (
    ('client', 'Client'),
    ('vendeur', 'Vendeur'),
)

# Modèle de profil central pour gérer les rôles
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    # Les champs spécifiques aux clients ou vendeurs seront ajoutés ici plus tard
    # selon le rôle

    def __str__(self):
        return f"Profil de {self.user.username} ({self.get_role_display()})"


# Modèle de profil pour les clients
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

# Modèle de profil pour les vendeurs
class Vendeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_entreprise = models.CharField(max_length=255, blank=True)
    numero_siret = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.nom_entreprise or self.user.username

# Modèle pour les messages de contact
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.nom} - {self.email}"
