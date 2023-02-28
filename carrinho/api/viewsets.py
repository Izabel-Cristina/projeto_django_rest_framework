from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from carrinho.models import Carrinho
from .serializers import CarrinhoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]




    # Sobrescrevendo uma ação Get (List)
    def list(self, request, *args, **kwargs):
        return super(CarrinhoViewSet, self).list(request, *args, **kwargs)

    # Sobrescrevendo uma ação Post
    def create(self, request, *args, **kwargs):
        return super(CarrinhoViewSet, self).create(request, *args, **kwargs)

    # Sobrescrevendo uma ação delete:
    def destroy(self, request, *args, **kwargs):
        return super(CarrinhoViewSet, self).destroy(request, *args, **kwargs)

    # Sobrevescrevendo o retrieve, update, partial_update
    def retrieve(self, request, *args, **kwargs):
        return super(CarrinhoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(CarrinhoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(CarrinhoViewSet, self).partial_update(request, *args, **kwargs)