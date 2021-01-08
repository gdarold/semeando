

# Register your models here.
from django.contrib import admin

from .models import Doacao, TipoPlantas, TipoDoacoes


@admin.register(TipoPlantas)
class PlantasAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug", "created", "modified"]


@admin.register(TipoDoacoes)
class DoacoesAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug", "created", "modified"]


@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = [
        "doador",
        "tipo_doacao",
        "tipo_planta",
        "descricao",
        "slug",
        "imagem",
        "peso",
        "quantidade",
        "is_available",
        "created",
        "modified",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["peso", "is_available"]
