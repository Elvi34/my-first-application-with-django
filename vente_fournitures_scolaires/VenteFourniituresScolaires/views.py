from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Produits.models import Produit
from Produits.forms import ProduitForm
# Create your views here.



class Login(TemplateView):
    template_name = "index.html"
    

class signup(TemplateView):
    template_name = "index.html"

class liste_produits(TemplateView):
    template_name = "produits.html"


def liste_produits(request):
    produits = Produit.objects.all()

    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()

    return render(request, 'Produits.html', {'produits': produits, 'form': form})

 

def Produit(request):
    return render(request, 'Produits.html')