# encoding=utf-8

from __future__ import unicode_literals

from django.db import models


class Sport(models.Model):
    name = models.CharField('Nome', max_length=100)
    duration_time = models.DecimalField('Duração geral (min)', max_digits=10, decimal_places=0)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Esporte'
        verbose_name_plural = 'Esportes'


class Game(models.Model):
    name = models.CharField('Nome', max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Em Breve', 'Em Breve'),
        ('Em Andamento', 'Em Andamento'),
        ('Terminado', 'Terminado'),
    )
    status = models.CharField('Status', default='Em Breve', choices=STATUS_CHOICES, max_length=100)
    start = models.DateTimeField('Começa em', null=True)
    score_red = models.DecimalField('Pontos Time Vermelho', max_digits=10, decimal_places=0, null=True)
    score_blue = models.DecimalField('Pontos Time Azul', max_digits=10, decimal_places=0, null=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
