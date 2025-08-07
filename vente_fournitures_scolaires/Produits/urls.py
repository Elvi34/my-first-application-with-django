from django.urls import path
from . import views
from .views import liste_produits
urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('product/', views.product, name='list'),
    
]



