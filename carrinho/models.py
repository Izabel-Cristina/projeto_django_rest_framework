from django.db import models
from produtos.models import Produto

# Create your models here.
class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.CASCADE)
    quantidade_compra = models.PositiveIntegerField()




