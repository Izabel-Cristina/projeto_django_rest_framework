from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from carrinho.models import Carrinho
from produtos.api.serializers import ProdutoSerializer

class CarrinhoSerializer(ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model= Carrinho
        fields ='__all__'
