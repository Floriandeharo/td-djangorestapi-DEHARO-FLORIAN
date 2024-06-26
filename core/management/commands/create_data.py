# core/management/commands/create_data.py

from django.core.management.base import BaseCommand
from core.models import Chercheur, ProjetDeRecherche, Publication
from django.utils import timezone

class Command(BaseCommand):
    help = 'Crée des données de test pour l\'application'

    def handle(self, *args, **kwargs):
        Chercheur.objects.all().delete()
        ProjetDeRecherche.objects.all().delete()
        Publication.objects.all().delete()
        
        # Création de chercheurs
        chercheur1 = Chercheur.objects.create(nom='Alice', specialite='Informatique')
        chercheur2 = Chercheur.objects.create(nom='Bob', specialite='Biologie')

        # Création de projets de recherche
        projet1 = ProjetDeRecherche.objects.create(
            titre='Projet A',
            description='Description du Projet A',
            date_debut=timezone.now(),
            date_fin_prevue=timezone.now().date(),
            chef_de_projet=chercheur1  # Associé un chercheur comme chef de projet
        )

        projet2 = ProjetDeRecherche.objects.create(
            titre='Projet B',
            description='Description du Projet B',
            date_debut=timezone.now(),
            date_fin_prevue=timezone.now().date(),
            chef_de_projet=chercheur2  # Associé un autre chercheur comme chef de projet
        )
        
                # Création de publications associées aux projets de recherche
        publication1 = Publication.objects.create(
            titre='Publication 1',
            resume='Résumé de la Publication 1',
            date_publication='2024-09-15',
            projet_associe=projet1  # Associer cette publication au projet 1
        )

        publication2 = Publication.objects.create(
            titre='Publication 2',
            resume='Résumé de la Publication 2',
            date_publication='2024-10-20',
            projet_associe=projet2  # Associer cette publication au projet 2
        )
        
        self.stdout.write(self.style.SUCCESS('Données créées avec succès'))
