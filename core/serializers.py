# core/serializers.py

from rest_framework import serializers
from .models import Chercheur, ProjetDeRecherche, Publication

class ChercheurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chercheur
        fields = '__all__'

class ProjetDeRechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetDeRecherche
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
