from rest_framework.serializers import ModelSerializer
from core.models import Ecommerce
class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model= Ecommerce
        fields ='produto', 'carrinho'