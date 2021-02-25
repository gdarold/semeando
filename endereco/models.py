from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel


from users.models import User


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Endereco(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cep = models.CharField("Cep", max_length=20)
    logradouro = models.CharField("Endereço", max_length=255)
    bairro = models.CharField("Bairro", max_length=255)
    numero = models.CharField("Número", max_length=255, default='0')
    complemento = models.CharField("Complemento", max_length=255, null=True, blank=True)
    cidade = models.CharField("Cidade",max_length=255)
    uf = models.CharField("Estado", max_length=255)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("cep",)

    def __str__(self):
        return self.cep

    def get_absolute_url(self):
        return reverse("users:profile")
