from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Carrinho
from produtos.models import Produto

# Create your views here.
class CarrinhoView(APIView):

    def get(self, request):
        carrinho = Carrinho.objects.all()
        produto = Produto.objects.all()
        total = (carrinho.quantidade_compra * produto.preco)
        for item in total:
            return Response({'item': item})

        return total