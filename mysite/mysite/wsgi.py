"""
Configuration WSGI pour le projet mysite.

Il expose l'objet WSGI appelable comme une variable de module nommée ``application``.

Pour plus d'informations sur ce fichier, voir :
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
