from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from users.models import User


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Cidade(TimeStampedModel):
    nome = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    class Meta:
        ordering = ("nome",)
        verbose_name = "cidade"
        verbose_name_plural = "cidades"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("endereco:list_by_cidade", kwargs={"slug": self.slug})


class Estado(TimeStampedModel):
    nome = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    class Meta:
        ordering = ("nome",)
        verbose_name = "estado"
        verbose_name_plural = "estados"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("endereco:list_by_estado", kwargs={"slug": self.slug})


class Endereco(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255, default='0')
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.ForeignKey(Cidade, related_name="endereco", on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="cidade")
    uf = models.ForeignKey(Estado, related_name="endereco", on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("cep",)

    def __str__(self):
        return self.cep

    def get_absolute_url(self):
        return reverse("endereco:detail", kwargs={"slug": self.slug})
