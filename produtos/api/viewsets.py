from rest_framework.viewsets import ModelViewSet
from produtos.models import Produto
from .serializers import ProdutoSerializer

class ProdutosViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer