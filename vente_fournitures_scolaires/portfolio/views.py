from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Projet

def portfolio_view(request):
    projets = Projet.objects.all()
    return render(request, 'portfolio.html', {'projets': projets})


