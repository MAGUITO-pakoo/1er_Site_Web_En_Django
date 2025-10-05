from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Adresse e-mail")  # champ email avec étiquette traduite

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]  # champs du formulaire d'inscription


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # champs modifiables pour l'utilisateur
