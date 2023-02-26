from django.db import models
from produtos.models import Produtos

# Create your models here.
class Carrinho(models.Model):
    id = models.IntegerField(primary_key=True)
    produtos = models.ForeignKey(Produtos, null=True, blank=True, on_delete=models.CASCADE)
    preco = models.DecimalField( max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()

    @property
    def descricao_completa2(self):
        return '%s - %s' % (self.nome, self.preco)

    def __str__(self):
        return '%s' %(self.produtos)




