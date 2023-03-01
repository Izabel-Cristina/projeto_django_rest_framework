from rest_framework.serializers import ModelSerializer
from produtos.models import Produto
from rest_framework.fields import SerializerMethodField


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model=Produto
        fields = ('id','nome', 'preco', 'quantidade_estoque','image')



