"""
Configuration des URLs du projet mysite

La liste `urlpatterns` route les URLs vers les vues. Pour plus d'informations, voir :
    https://docs.djangoproject.com/en/2.2/topics/http/urls/

Exemples :
Vues basées sur fonctions
    1. Ajouter un import : from my_app import views
    2. Ajouter une URL à urlpatterns : path('', views.home, name='home')

Vues basées sur classes
    1. Ajouter un import : from other_app.views import Home
    2. Ajouter une URL à urlpatterns : path('', Home.as_view(), name='home')

Inclure un autre URLconf
    1. Importer la fonction include() : from django.urls import include, path
    2. Ajouter une URL à urlpatterns : path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls"))
]

# début
