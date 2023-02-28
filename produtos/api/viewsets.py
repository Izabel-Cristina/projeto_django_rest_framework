from rest_framework.viewsets import ModelViewSet
from produtos.models import Produto
from .serializers import ProdutoSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [filters.SearchFilter]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']