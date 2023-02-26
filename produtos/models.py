from django.db import models

# Create your models here.
class Produtos(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    quantidade_estoque = models.IntegerField()
    preco = models.DecimalField( max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='ecommerce', null=True, blank=True)

    def __str__(self):
        return self.nome






