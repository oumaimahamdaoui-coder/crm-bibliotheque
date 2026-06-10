from django.core.exceptions import ValidationError
from django.db import models


class Livre(models.Model):
    livre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.livre


class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    nom_etudiant = models.CharField(max_length=100)

    date_emprunt = models.DateField()
    date_retour_prevue = models.DateField()
    date_retour_reelle = models.DateField(null=True, blank=True)

    def clean(self):
        if self.date_retour_reelle and self.date_retour_reelle < self.date_emprunt:
            raise ValidationError(
                "❌ La date de retour ne peut pas être avant la date d'emprunt"
            )

    @property
    def jours_retard(self):
        if self.date_retour_reelle and self.date_retour_reelle > self.date_retour_prevue:
            return (self.date_retour_reelle - self.date_retour_prevue).days
        return 0

    @property
    def amende(self):
        return self.jours_retard * 5

    def __str__(self):
        return self.nom_etudiant
