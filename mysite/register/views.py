from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Création des vues pour l'inscription
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)  # création du formulaire d'inscription
        if form.is_valid():
            form.save()  # sauvegarde du nouvel utilisateur
            return redirect("/home")  # redirection vers la page d'accueil
    else:
        form = UserCreationForm()  # formulaire vide pour GET

    return render(response, "register/register.html", {"form": form})  # rendu du template d'inscription
