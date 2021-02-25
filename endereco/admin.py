from django.contrib import admin

# Register your models here.
from endereco.models import Endereco


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "usuario",
        "cep",
        "logradouro",
        "bairro",
        "numero",
        "complemento",

         "uf",
        "is_available",
        "created",
        "modified",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["logradouro", "is_available"]
