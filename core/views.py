# core/views.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Chercheur, ProjetDeRecherche, Publication
from .serializers import ChercheurSerializer, ProjetDeRechercheSerializer, PublicationSerializer
from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import UpdateView
from .forms import ChercheurForm, ProjetDeRechercheForm, PublicationForm, ProjetDeRechercheFilterForm, PublicationFilterForm, ChercheurFilterForm
from django.views.generic import CreateView
from .filters import ProjetDeRechercheFilter, PublicationFilter
from django.contrib.auth.decorators import login_required

class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer
    
class ChercheurCreateView(CreateView):
    model = Chercheur
    form_class = ChercheurForm
    template_name = 'chercheur/new_chercheur_form.html'
    success_url = reverse_lazy('liste_chercheurs')    

class ChercheurUpdateView(UpdateView):
    model = Chercheur
    form_class = ChercheurForm
    template_name = 'chercheur/chercheur_form.html'
    success_url = reverse_lazy('liste_chercheurs')
    
class ChercheurDeleteView(DeleteView):
    model = Chercheur

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Le chercheur a été supprimé avec succès.'})
        
    def get_success_url(self):
        return reverse_lazy('liste_chercheurs')    
    
    
    
class ProjetDeRechercheCreateView(CreateView):
    model = ProjetDeRecherche
    form_class = ProjetDeRechercheForm
    template_name = 'projet/projet_new_form.html'
    success_url = reverse_lazy('liste_projets')

class ProjetDeRechercheUpdateView(UpdateView):
    model = ProjetDeRecherche
    form_class = ProjetDeRechercheForm
    template_name = 'projet/projet_form.html'
    success_url = reverse_lazy('liste_projets')

class ProjetDeRechercheDeleteView(DeleteView):
    model = ProjetDeRecherche

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Le projet a été supprimé avec succès.'})

    def get_success_url(self):
        return reverse_lazy('liste_projets')

class ProjetDeRechercheViewSet(viewsets.ModelViewSet):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titre', 'date_debut', 'date_fin_prevue']



class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titre', 'date_publication']

class PublicationCreateView(CreateView):
        model = Publication
        form_class = PublicationForm
        template_name = 'publication/publication_new_form.html'
        success_url = reverse_lazy('liste_publications')

class PublicationUpdateView(UpdateView):
        model = Publication
        form_class = PublicationForm
        template_name = 'publication/publication_form.html'
        success_url = reverse_lazy('liste_publications')

class PublicationDeleteView(DeleteView):
        model = Publication

        def delete(self, request, *args, **kwargs):
            self.object = self.get_object()
            self.object.delete()
            return JsonResponse({'message': 'La publication a été supprimée avec succès.'})

        def get_success_url(self):
            return reverse_lazy('liste_publications')

class PublicationViewSet(viewsets.ModelViewSet):
        queryset = Publication.objects.all()
        serializer_class = PublicationSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['titre', 'date_publication']
        
        

def filtrer_projets(request):
    queryset = ProjetDeRecherche.objects.all()
    filtered = False

    if request.method == 'POST':
        form = ProjetDeRechercheFilterForm(request.POST)
        if form.is_valid():
            queryset = form.filter(queryset)
            filtered = True
    else:
        form = ProjetDeRechercheFilterForm()

    context = {
        'form': form,
        'filtered': filtered,
        'projets': queryset
    }

    return render(request, 'projet/filtre.html', context)


def index(request):
    return render(request, 'index.html')

# chercheur

def liste_chercheurs(request):
    queryset = Chercheur.objects.all()
    filtered = False
    form = ChercheurFilterForm(request.GET or None)

    if form.is_valid():
        queryset = form.filter(queryset)
        filtered = True

    context = {
        'form': form,
        'filtered': filtered,
        'chercheurs': queryset
    }

    return render(request, 'chercheur/index.html', context)

def chercheur_form(request):
    return render(request, 'chercheur/chercheur_form.html')

# projet 

def liste_projets(request):
    queryset = ProjetDeRecherche.objects.all()
    filtered = False
    form = ProjetDeRechercheFilterForm(request.GET or None)

    if form.is_valid():
        queryset = form.filter(queryset)
        filtered = True

    context = {
        'form': form,
        'filtered': filtered,
        'projets': queryset
    }

    return render(request, 'projet/index.html', context)

def projet_form(request):
    return render(request, 'projet/projet_form.html')

# publication
@login_required
def liste_publications(request):

    queryset = Publication.objects.all()
    filtered = False
    form = PublicationFilterForm(request.GET or None)

    if form.is_valid():
        queryset = form.filter(queryset)
        filtered = True

    context = {
        'form': form,
        'filtered': filtered,
        'publications': queryset
    }

    return render(request, 'publication/index.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie.')
            return redirect('index')  # Rediriger vers la page d'accueil après la connexion
        else:
            messages.error(request, 'Identifiants invalides.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Déconnexion réussie.')
    return redirect('index')  # Rediriger vers la page d'accueil après la déconnexion

def publication_form(request):
    return render(request, 'publication/publication_form.html')
