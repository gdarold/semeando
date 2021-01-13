from django.contrib import admin

# Register your models here.
from endereco.models import Endereco, Cidade, Estado


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug", "created", "modified"]


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug", "created", "modified"]


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        "usuario",
        "cep",
        "logradouro",
        "bairro",
        "numero",
        "complemento",
        "cidade",
        "slug",
        "uf",
        "is_available",
        "created",
        "modified",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["logradouro", "is_available"]
