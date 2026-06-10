from django import forms
from .models import Livre, Emprunt

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['livre', 'auteur']


class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = [
            'livre',
            'nom_etudiant',
            'date_emprunt',
            'date_retour_prevue',
            'date_retour_reelle'
        ]
