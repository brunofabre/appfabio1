from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=100, unique=True)
    backgroud = models.CharField('Fundo', max_length=100)
    front = models.CharField('Frente', max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    ra = models.CharField('RA', max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
