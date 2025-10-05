from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']  # champs affichés dans l'administration

# Enregistrement du modèle utilisateur personnalisé dans l'admin Django
admin.site.register(CustomUser, CustomUserAdmin)
