from typing import Type
from produtos import Produto

class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = [] # coleção

    def adicionar_produto(self, produto: Type[Produto]) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self):
        print("Compra finalizada")

        for produto in self.__produtos:
            produto.informacoes_produto()

        self.__produtos = [] # limpar nosso vetor
