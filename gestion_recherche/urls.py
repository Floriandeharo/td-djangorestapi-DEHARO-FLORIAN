"""gestion_recherche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# gestion_recherche/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token  # Pour l'obtention du token si nécessaire
from django.contrib.auth import views as auth_views

from core.views import index

schema_view = get_schema_view(
   openapi.Info(
      title="Gestion de Recherche API",
      default_version='v1',
      description="Documentation de l'API pour la gestion de recherche",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),  # Endpoint pour l'obtention du token si nécessaire
    path('accounts/', include('django.contrib.auth.urls')),  # Inclut les URLs de gestion d'authentification Django
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', index, name='index'),  # Route racine vers votre vue personnalisée
    path('api/', include('core.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
