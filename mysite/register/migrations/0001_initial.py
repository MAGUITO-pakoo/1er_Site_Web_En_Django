# Généré par Django 2.2 le 2024-04-29 15:20

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='mot de passe')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='dernière connexion')),
                ('is_superuser', models.BooleanField(
                    default=False,
                    help_text="Indique que cet utilisateur dispose de tous les droits sans qu'ils soient explicitement assignés.",
                    verbose_name='statut superutilisateur'
                )),
                ('username', models.CharField(
                    error_messages={'unique': "Un utilisateur avec ce nom d'utilisateur existe déjà."},
                    help_text="Requis. 150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement.",
                    max_length=150,
                    unique=True,
                    validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                    verbose_name="nom d'utilisateur"
                )),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='prénom')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='nom')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='adresse e-mail')),
                ('is_staff', models.BooleanField(
                    default=False,
                    help_text="Indique si l'utilisateur peut se connecter au site d'administration.",
                    verbose_name='statut du personnel'
                )),
                ('is_active', models.BooleanField(
                    default=True,
                    help_text="Indique si cet utilisateur doit être traité comme actif. Désélectionnez plutôt que de supprimer le compte.",
                    verbose_name='actif'
                )),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now,
                    verbose_name="date d'inscription"
                )),
                ('groups', models.ManyToManyField(
                    blank=True,
                    help_text="Les groupes auxquels appartient cet utilisateur. Un utilisateur reçoit tous les droits accordés à chacun de ses groupes.",
                    related_name='user_set',
                    related_query_name='user',
                    to='auth.Group',
                    verbose_name='groupes'
                )),
                ('toDoLists', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='main.ToDoList'
                )),
                ('user_permissions', models.ManyToManyField(
                    blank=True,
                    help_text="Permissions spécifiques pour cet utilisateur.",
                    related_name='user_set',
                    related_query_name='user',
                    to='auth.Permission',
                    verbose_name="permissions utilisateur"
                )),
            ],
            options={
                'verbose_name': 'utilisateur',
                'verbose_name_plural': 'utilisateurs',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
