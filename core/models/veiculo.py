from django.db import models
from .cor import Cor
from .modelo import Modelo
from .acessorio import Acessorio
from core.models import acessorio

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculo", null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo", null=True, blank=True)
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10,decimal_places=2, null=True, default=0)
    acessorio = models.ManyToManyField(Acessorio, related_name='veiculo', blank=True)



    def __str__(self):
        return f"{self.id}"