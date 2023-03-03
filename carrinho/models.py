from django.db import models
from django.contrib.auth.models import User

from produtos.models import Produto

# Create your models here.
class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.CASCADE)
    quantidade_compra = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)






