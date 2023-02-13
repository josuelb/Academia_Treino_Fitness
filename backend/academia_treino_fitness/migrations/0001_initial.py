# Generated by Django 4.1.6 on 2023-02-13 13:32

import academia_treino_fitness.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('remuneracao', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plano', models.CharField(max_length=50)),
                ('valor', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to=academia_treino_fitness.models.Photo)),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.IntegerField(unique=True)),
                ('user', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('cargo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='academia_treino_fitness.cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to=academia_treino_fitness.models.Photo)),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('data_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.IntegerField(unique=True)),
                ('user', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('situacao', models.CharField(max_length=7)),
                ('objetivo', models.CharField(max_length=100)),
                ('plano', models.ForeignKey(default='Mensal', on_delete=django.db.models.deletion.CASCADE, to='academia_treino_fitness.plano')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]