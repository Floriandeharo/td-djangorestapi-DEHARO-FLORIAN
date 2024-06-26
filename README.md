Projet Gestion de Recherche
Ce projet utilise Django pour gérer une application de gestion de chercheurs, projets de recherche et publications.

Fonctionnalités

Affichage, création, modification et suppression de chercheurs, projets de recherche et publications via l'API et l'interface web.
Filtrage des projets de recherche et publications par divers critères tels que dates, chercheur impliqué ou titre de projet.
Authentification utilisateur.
Utilisation de vues basées sur les classes pour les opérations CRUD.
Prérequis
Avant de commencer, assurez-vous d'avoir installé :

Python (version 3.x)
Django (version 3.x)

Installation
Clonez le repository depuis GitHub :

Copier le code
git clone https://github.com/votre-utilisateur/gestion_recherche.git
cd gestion_recherche

Installez les dépendances Python :

Copier le code
pip install -r requirements.txt
Configuration

Configurez la base de données dans le fichier settings.py :

Copier le code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Appliquez les migrations initiales pour créer les tables de base de données :

Copier le code
python manage.py migrate
Lancement du Serveur
Pour démarrer le serveur de développement Django, utilisez la commande suivante :

Copier le code
python manage.py runserver
Le serveur sera accessible à l'adresse http://localhost:8000/.

Utilisation
Accédez à l'interface web de l'application en ouvrant votre navigateur et en naviguant vers http://localhost:8000/.
Pour utiliser l'API, consultez la documentation fournie ou accédez directement aux endpoints à partir de http://localhost:8000/api/.

Auteurs
Deharo Florian 
Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

