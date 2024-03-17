from typing import Dict, Type
from model.repositorio import Repositorio

class Insersor:
    # injeção da dependência do tipo obj Repositorio
    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repo = repositorio

    def inserir_dado(self, nome: str, idade: int) -> Dict:
        registro = self.__repo.select(nome)

        if registro:
            raise Exception("O registro já exite")
        
        novo_registro = self.__repo.insert(nome, idade)
        return novo_registro