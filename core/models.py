# core/models.py

from django.db import models

class Chercheur(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    projets = models.ManyToManyField('ProjetDeRecherche', related_name='chercheurs', blank=True)

    def __str__(self):
        return self.nom

class ProjetDeRecherche(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin_prevue = models.DateField()
    chef_de_projet = models.ForeignKey(Chercheur, on_delete=models.CASCADE, related_name='projets_chef')

    def __str__(self):
        return self.titre

class Publication(models.Model):
    titre = models.CharField(max_length=200)
    resume = models.TextField()
    projet_associe = models.ForeignKey(ProjetDeRecherche, on_delete=models.CASCADE, related_name='publications')
    date_publication = models.DateField()

    def __str__(self):
        return self.titre
