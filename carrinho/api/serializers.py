from rest_framework.serializers import ModelSerializer
from carrinho.models import Carrinho
from produtos.api.serializers import ProdutoSerializer

class CarrinhoSerializer(ModelSerializer):
    produto = ProdutoSerializer(many=True)
    class Meta:
        model= Carrinho
        fields = ('produto', 'quantidade')