from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email',
        'password',
        'situacao',
        'plano',
        'objetivo'
    )
    list_display_links = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email'
    )
    search_fields = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email',
        'password',
        'situacao',
        'plano',
        'objetivo'
    )


@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email',
        'password',
        'cargo'
    )
    list_display_links = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email'
    )
    search_fields = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email',
        'password',
        'cargo'
    )


@admin.register(Cargo)
class Cargo(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'remuneracao'
    )
    list_display_links = ('id', 'nome', 'remuneracao')
    search_fields = (
        'id',
        'nome',
        'remuneracao'
    )


@admin.register(Plano)
class Plano(admin.ModelAdmin):
    list_display = ('id', 'plano', 'valor')
    list_display_links = ('id',)
    search_fields = ('id', 'plano', 'valor')
