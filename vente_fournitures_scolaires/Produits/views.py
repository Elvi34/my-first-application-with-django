from django.shortcuts import render, redirect
from .models import Produit
from .forms import ProduitForm

# Create your views here.

def liste_produits(request):
    produits = Produit.objects.all()

    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()

    return render(request, 'produits/produits.html', {'produits': produits, 'form': form})


def ajouter_produit(request):
    
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produit')
    else:
        form = ProduitForm()
    return render(request, 'produits/produits.html')

def modifier_produits(request, pk):
   
    form = ProduitsForm(request.POST or None, request.FILES or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('liste_articles')
    return render(request, 'produits/produits.html', {'form': form})

def supprimer_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('liste_articles')


from django.shortcuts import render
from .models import Produit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product(request):
    # Récupérer tous les produits
    produits_list = Produit.objects.all()
    
    # Nombre d'éléments par page
    items_per_page = 12
    
    # Initialisation du paginator
    paginator = Paginator(produits_list, items_per_page)
    
    # Récupération du numéro de page depuis la requête GET
    page_number = request.GET.get('page')
    
    try:
        # Essayer de récupérer la page demandée
        produits = paginator.page(page_number)
    except PageNotAnInteger:
        # Si le paramètre page n'est pas un entier, afficher la première page
        produits = paginator.page(1)
    except EmptyPage:
        # Si la page est hors limite (trop grande), afficher la dernière page
        produits = paginator.page(paginator.num_pages)
    
    # Filtrage par recherche si paramètre présent
    search_query = request.GET.get('search')
    if search_query:
        produits = produits.filter(nom__icontains=search_query)
    
    context = {
        'produits': produits,
        'page_obj': produits,  # Pour la pagination dans le template
    }
    
    return render(request, 'produitspossibles.html', context)





from django.shortcuts import render
from .models import Produit

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/produitspossibles.html', {'produits': produits})
