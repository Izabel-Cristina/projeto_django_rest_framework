from rest_framework.views import APIView
from rest_framework.response import Response
from carrinho.models import Carrinho
from carrinho.api.serializers import CarrinhoSerializer

# Create your views here.
class CarrinhoView(APIView):
    def get(self, *args, **kwargs):
        carrinho = Carrinho.objects.all().select_related('produto')
        serializer = CarrinhoSerializer

        id = kwargs.get('id', '')

        if id:
            try:
                carrinho = carrinho.get(id=id)
                carrinho_json = serializer(carrinho).data
            except:
                return Response({'msg':'carrinho não encontrado'}, status=404)
            return Response(carrinho_json)

        carrinho_json = serializer(carrinho, many=True).data
        return Response(carrinho_json)