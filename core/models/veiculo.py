from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10,decimal_places=2, null=True, default=0)


    def __str__(self):
        return f"{self.id}"