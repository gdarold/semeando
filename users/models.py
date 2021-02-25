from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    cpf = models.CharField(max_length=12, blank=False, null=False)
    telefone = models.CharField(max_length=20, blank=False, null=False)
    com_endereco = models.BooleanField(default=False)
