


from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w-full border px-4 py-2 rounded focus:ring focus:ring-blue-200'}),
            'description': forms.Textarea(attrs={'class': 'w-full border px-4 py-2 rounded focus:ring focus:ring-blue-200'}),
            'prix': forms.NumberInput(attrs={'class': 'w-full border px-4 py-2 rounded focus:ring focus:ring-blue-200'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full border px-4 py-2 rounded focus:ring focus:ring-blue-200'}),
        }