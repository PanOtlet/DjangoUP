from django.db import models
from .helpers import RandomFileName


class SEOMeta(models.Model):
    website = models.CharField('Nazwa strony', max_length=50)
    title = models.CharField('Meta tytuł', max_length=120)
    meta_description = models.CharField('Meta Opis', max_length=170)
    keywords = models.TextField('Słowa kluczowe')

    class Meta:
        verbose_name = 'Ustawienia Meta'
        verbose_name_plural = 'Ustawienia Meta'

    def __str__(self):
        return self.title
