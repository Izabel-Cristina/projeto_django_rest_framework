from rest_framework.serializers import ModelSerializer
from carrinho.models import Carrinho

class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model= Carrinho
        fields = ('id','produtos', 'quantidade', 'preco')