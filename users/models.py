from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    cpf = models.TextField(max_length=12, blank=False, null=False)
    telefone = models.TextField(max_length=20, blank=False, null=False)
