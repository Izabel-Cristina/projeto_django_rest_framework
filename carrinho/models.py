from django.db import models
from produtos.models import Produto

# Create your models here.
class Carrinho(models.Model):
    produto = models.ManyToManyField(Produto, related_name='produto')
    quantidade = models.IntegerField()
    def __str__(self):
        return '%s' %(self.produto)




