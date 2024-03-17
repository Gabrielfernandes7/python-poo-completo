from abc import ABC, abstractmethod

"""
Não posso ter uma instância de uma classe abstrata

No python, para ter uma classe abstrata, 
devemos ter no mínimo um método abstrato
"""
class AbstractClass(ABC):
    def __init__(self) -> None:
        self.atributo = "Olá mundo"

    def metodo(self, elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass