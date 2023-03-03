from rest_framework.serializers import ModelSerializer
from carrinho.models import Carrinho
from produtos.api.serializers import ProdutoSerializer
from rest_framework import serializers

class CarrinhoSerializer(ModelSerializer):
    produto = ProdutoSerializer()
    total = serializers.SerializerMethodField()
    data = serializers.DateTimeField(format="%d-%m-%Y")

    def get_total(self, obj):
        return obj.produto.preco * obj.quantidade_compra
    class Meta:
        model= Carrinho
        fields =('user', 'produto','quantidade_compra', 'total', 'data')
