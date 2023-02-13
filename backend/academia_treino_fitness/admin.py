from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email'
    )
    search_fields = '__all__'


@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = (
        'id',
        'nome',
        'user',
        'cpf',
        'rg',
        'email'
    )
    search_fields = '__all__'


@admin.register(Cargo)
class Cargo(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = '__all__'
    search_fields = '__all__'


@admin.register(Plano)
class Plano(admin.ModelAdmin):
    list_display = '__all__'
    list_display_links = '__all__'
    search_fields = '__all__'
