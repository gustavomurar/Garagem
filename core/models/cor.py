from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f"({self.id}){self.nome.upper()}"