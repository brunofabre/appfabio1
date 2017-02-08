from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, unique=True)
