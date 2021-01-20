from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from users.models import User


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Endereco(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255, default='0')
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("cep",)

    def __str__(self):
        return self.cep

    def get_absolute_url(self):
        return reverse("endereco:list")
