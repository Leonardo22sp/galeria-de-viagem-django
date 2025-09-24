from django.db import models
from datetime import date


CONTINENTES = [
    ("america-do-sul", "América do Sul"),
    ("america-do-norte", "América do Norte"),
    ("europa", "Europa"),
    ("asia", "Ásia"),
    ("africa", "África"),
    ("oceania", "Oceania"),
    ("antartida", "Antártida"),
]

ESTILOS = [
    ("paisagem", "Paisagem"),
    ("retratos", "Retratos"),
    ("urbano", "Urbano"),
    ("natureza", "Natureza"),
    ("cultural", "Cultural"),
    ("aventura", "Aventura"),
]


class Foto(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False)
    continente = models.CharField(max_length=30, choices=CONTINENTES, default="america-do-sul")
    estilo = models.CharField(max_length=30, choices=ESTILOS, default="paisagem")
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    data_viagem = models.DateField(default=date.today)
    publicada = models.BooleanField(default=True)

    destaque = models.BooleanField(default=False, help_text="Marque para que esta foto possa aparecer na página inicial.")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-data_viagem']