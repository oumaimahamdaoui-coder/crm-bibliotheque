from django.contrib import admin
from .models import Livre, Emprunt


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('id', 'livre', 'auteur', 'isbn')
    search_fields = ('livre', 'auteur', 'isbn')


@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = (
        'nom_etudiant',
        'livre',
        'date_emprunt',
        'date_retour_prevue',
        'date_retour_reelle',
        'jours_retard',
        'amende',
    )

    search_fields = ('nom_etudiant', 'livre__titre')
    list_filter = ('date_emprunt', 'date_retour_prevue')
