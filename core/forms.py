# core/forms.py

from django import forms
from .models import Chercheur, ProjetDeRecherche, Publication

class ChercheurForm(forms.ModelForm):
    class Meta:
        model = Chercheur
        fields = ['nom', 'specialite']

class ProjetDeRechercheForm(forms.ModelForm):
    class Meta:
        model = ProjetDeRecherche
        fields = ['titre', 'description', 'date_debut', 'date_fin_prevue', 'chef_de_projet']
        
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['titre', 'resume', 'date_publication', 'projet_associe']
        

class ProjetDeRechercheFilterForm(forms.Form):
    titre = forms.CharField(required=False)
    date_debut_min = forms.DateField(required=False, label='Date de début minimale', widget=forms.TextInput(attrs={'type': 'date'}))
    date_debut_max = forms.DateField(required=False, label='Date de début maximale', widget=forms.TextInput(attrs={'type': 'date'}))
    date_fin_min = forms.DateField(required=False, label='Date de fin prévue minimale', widget=forms.TextInput(attrs={'type': 'date'}))
    date_fin_max = forms.DateField(required=False, label='Date de fin prévue maximale', widget=forms.TextInput(attrs={'type': 'date'}))
    chef_de_projet = forms.ModelChoiceField(queryset=Chercheur.objects.all(), required=False, label='Chef de projet')

    def filter(self, queryset):
        if self.is_valid():
            titre = self.cleaned_data.get('titre')
            date_debut_min = self.cleaned_data.get('date_debut_min')
            date_debut_max = self.cleaned_data.get('date_debut_max')
            date_fin_min = self.cleaned_data.get('date_fin_min')
            date_fin_max = self.cleaned_data.get('date_fin_max')
            chef_de_projet = self.cleaned_data.get('chef_de_projet')

            if titre:
                queryset = queryset.filter(titre__icontains=titre)
            if date_debut_min:
                queryset = queryset.filter(date_debut__gte=date_debut_min)
            if date_debut_max:
                queryset = queryset.filter(date_debut__lte=date_debut_max)
            if date_fin_min:
                queryset = queryset.filter(date_fin_prevue__gte=date_fin_min)
            if date_fin_max:
                queryset = queryset.filter(date_fin_prevue__lte=date_fin_max)
            if chef_de_projet:
                queryset = queryset.filter(chef_de_projet=chef_de_projet)

        return queryset

class PublicationFilterForm(forms.Form):
    titre = forms.CharField(required=False)
    date_publication_min = forms.DateField(required=False, label='Date de publication minimale', widget=forms.TextInput(attrs={'type': 'date'}))
    date_publication_max = forms.DateField(required=False, label='Date de publication maximale', widget=forms.TextInput(attrs={'type': 'date'}))
    projet_associe = forms.ModelChoiceField(queryset=ProjetDeRecherche.objects.all(), required=False, label='Projet associé')

    def filter(self, queryset):
        if self.is_valid():
            titre = self.cleaned_data.get('titre')
            date_publication_min = self.cleaned_data.get('date_publication_min')
            date_publication_max = self.cleaned_data.get('date_publication_max')
            
            projet_associe = self.cleaned_data.get('projet_associe')

            if titre:
                queryset = queryset.filter(titre__icontains=titre)
            if date_publication_min:
                queryset = queryset.filter(date_publication__gte=date_publication_min)
            if date_publication_max:
                queryset = queryset.filter(date_publication__lte=date_publication_max)
            if projet_associe:
                queryset = queryset.filter(projet_associe=projet_associe)

        return queryset

class ChercheurFilterForm(forms.Form):
    nom = forms.CharField(required=False)
    specialite = forms.CharField(required=False)

    def filter(self, queryset):
        if self.is_valid():
            nom = self.cleaned_data.get('nom')
            specialite = self.cleaned_data.get('specialite')

            if nom:
                queryset = queryset.filter(nom__icontains=nom)
            if specialite:
                queryset = queryset.filter(specialite__icontains=specialite)

        return queryset
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)