from django import forms
from .models import Commande

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['adresse_livraison','adresse_facturation','meth_paiemet']