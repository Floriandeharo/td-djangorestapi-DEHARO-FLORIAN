# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChercheurViewSet, ProjetDeRechercheViewSet, PublicationViewSet, index, chercheur_form, projet_form, publication_form, ChercheurUpdateView, ChercheurCreateView
from . import views

router = DefaultRouter()
router.register(r'chercheurs', ChercheurViewSet)
router.register(r'projets', ProjetDeRechercheViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('', index, name='index'),

    
    path('chercheur/', views.liste_chercheurs, name='liste_chercheurs'),
    path('chercheur/<int:pk>/supprimer/', views.ChercheurDeleteView.as_view(), name='supprimer_chercheur'),
    path('chercheur/<int:pk>/modifier/', ChercheurUpdateView.as_view(), name='modifier_chercheur'),
    path('chercheur/ajouter/', ChercheurCreateView.as_view(), name='ajouter_chercheur'),

    path('projet/', views.liste_projets, name='liste_projets'),
    path('projet/<int:pk>/supprimer/', views.ProjetDeRechercheDeleteView.as_view(), name='supprimer_projet'),
    path('projet/<int:pk>/modifier/', views.ProjetDeRechercheUpdateView.as_view(), name='modifier_projet'),
    path('projet/ajouter/', views.ProjetDeRechercheCreateView.as_view(), name='ajouter_projet'),

    path('publication/', views.liste_publications, name='liste_publications'),
    path('publication/<int:pk>/supprimer/', views.PublicationDeleteView.as_view(), name='supprimer_publication'),
    path('publication/<int:pk>/modifier/', views.PublicationUpdateView.as_view(), name='modifier_publication'),
    path('publication/ajouter/', views.PublicationCreateView.as_view(), name='ajouter_publication'),
]