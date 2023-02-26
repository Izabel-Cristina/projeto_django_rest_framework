from rest_framework.viewsets import ModelViewSet
from produtos.models import Produtos
from .serializers import ProdutosSerializer

class ProdutosViewSet(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer