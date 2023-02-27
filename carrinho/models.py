from django.db import models
from produtos.models import Produto

# Create your models here.
class Carrinho(models.Model):
    produto = models.ManyToManyField(Produto)
    quantidade = models.IntegerField()





