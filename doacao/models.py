from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from users.models import User


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class TipoPlantas(TimeStampedModel):
    nome = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    class Meta:
        ordering = ("nome",)
        verbose_name = "tipo_planta"
        verbose_name_plural = "tipos_plantas"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("doacao:list_by_tipo_planta", kwargs={"slug": self.slug})


class TipoDoacoes(TimeStampedModel):
    nome = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    class Meta:
        ordering = ("nome",)
        verbose_name = "tipo_doacao"
        verbose_name_plural = "tipos_doacoes"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("doacao:list_by_tipo_doacao", kwargs={"slug": self.slug})


class Doacao(TimeStampedModel):
    doador = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_doacao = models.ForeignKey(TipoDoacoes, related_name="doacao",
                                    on_delete=models.CASCADE)
    tipo_planta = models.ForeignKey(TipoPlantas, related_name="doacao",
                                    on_delete=models.CASCADE)
    descricao = models.TextField(blank=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="tipo_doacao")
    imagem = models.ImageField(upload_to="doacao/%Y/%m/%d", blank=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ("tipo_doacao",)

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse("doacao:detalhes", kwargs={"slug": self.slug})
