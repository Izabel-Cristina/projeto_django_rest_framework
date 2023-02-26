from rest_framework.serializers import ModelSerializer
from produtos.models import Produtos

class ProdutosSerializer(ModelSerializer):
    class Meta:
        model=Produtos
        fields = ('id','nome', 'preco', 'quantidade_estoque','image')