from django import forms
from .models import Commande

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['paid', 'adresse_livraison']