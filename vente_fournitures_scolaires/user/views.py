from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'


# Si tu as un formulaire personnalisé pour l'inscription, importe-le ici
from .forms import UserRegistrationForm

# Si tu as des modèles Profil, Client, importe-les
from .models import Profil, Client


def register(request):
    """
    Inscription avec formulaire personnalisé UserRegistrationForm
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Set password hashed
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Création des profils associés
            role = form.cleaned_data.get('role', 'client')  # Par défaut client
            Profil.objects.create(user=user, role=role)
            Client.objects.create(user=user)

            messages.success(request, "Inscription réussie, vous pouvez maintenant vous connecter.")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/inscription.html', {'form': form})


def inscription_view(request):
    """
    Inscription simple avec UserCreationForm (sans champs personnalisés)
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie, vous pouvez maintenant vous connecter.")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'inscription.html', {'form': form})


def connexion_view(request):
    """
    Connexion classique
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirection vers la page liste_produits après connexion
            return redirect('liste_produits')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'users/login.html')
