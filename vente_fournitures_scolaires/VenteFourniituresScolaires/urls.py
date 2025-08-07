from django.urls import path
from . import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('register/', views.signup.as_view(), name='signup'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produit/', views.Produit, name='produit'),  # Notez le nom 'produit' pour l'URL

    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
]


