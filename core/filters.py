# core/filters.py

import django_filters
from .models import ProjetDeRecherche, Publication

class ProjetDeRechercheFilter(django_filters.FilterSet):
    class Meta:
        model = ProjetDeRecherche
        fields = {
            'titre': ['icontains'],
            'date_debut': ['gte', 'lte'],
            'date_fin_prevue': ['gte', 'lte'],
            'chef_de_projet': ['exact'],
        }

class PublicationFilter(django_filters.FilterSet):
    class Meta:
        model = Publication
        fields = {
            'titre': ['icontains'],
            'date_publication': ['gte', 'lte'],
        }
