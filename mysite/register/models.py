from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import ToDoList

# Création des modèles
class CustomUser(AbstractUser):
    toDoLists = models.ForeignKey(
        ToDoList,
        on_delete=models.CASCADE,
        verbose_name="Listes de tâches"  # étiquette traduite
    )
