from django.db import models

# Create your models here.
from django.urls import reverse
from model_utils.models import TimeStampedModel

from users.models import User


class Endereco(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=255, default='0')
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('list_enderecos')


    def __str__(self):
        return self.cep