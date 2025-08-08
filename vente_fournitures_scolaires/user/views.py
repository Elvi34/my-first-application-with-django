from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profil, Client
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Rôle par défaut (caché dans le formulaire) : 'client'
            role = form.cleaned_data['role']
            Profil.objects.create(user=user, role=role)
            Client.objects.create(user=user)

            return redirect('login')  # redirige vers la page de connexion
    else:
        form = UserRegistrationForm()

    return render(request, 'users/.html', {'form': form})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'




def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('login')  # redirige vers la page de connexion
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = UserCreationForm()
    return render(request, 'inscription.html', {'form': form})






from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def connexion_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_produits')
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'user/login.html', {'error': error})
    return render(request, 'user/login.html')
