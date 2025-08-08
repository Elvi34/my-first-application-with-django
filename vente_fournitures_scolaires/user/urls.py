from django.urls import path
from .views import register, inscription_view, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),  # Si tu utilises cette vue (sinon supprimer)
    
    # Pour la connexion, tu peux choisir soit ta vue CustomLoginView, soit celle de Django
    path('login/', CustomLoginView.as_view(), name='login'),
    # ou (ne garde qu'une seule des deux) :
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),

    # Pour l'inscription, garde UNE seule ligne correcte :
    path('inscription/', inscription_view, name='inscription'),
]
