"""
iremos agregar classe ou objeto em outra classe
"""
from produtos import Produto
from carrinho import CarrinhoDeCompras

carr = CarrinhoDeCompras()
memoria_ram = Produto("Memória RAM", 150)
monitor = Produto("Monitor", 1000)

carr.adicionar_produto(memoria_ram)
carr.adicionar_produto(monitor)
carr.finalizar_compra()
