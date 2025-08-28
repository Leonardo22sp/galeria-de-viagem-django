from django.db import models
from datetime import date

class Foto(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    data_viagem = models.DateField(default=date.today)
    publicada = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-data_viagem']