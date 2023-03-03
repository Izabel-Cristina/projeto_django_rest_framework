from django.urls import path
from carrinho.views import CarrinhoView

urlpatterns = [
    path('valor/<int:id>', CarrinhoView.as_view()),
    path('valor/', CarrinhoView.as_view()),
]