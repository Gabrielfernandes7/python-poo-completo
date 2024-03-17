# Injeção de Dependência

A Injeção de Dependência é um padrão de design em que os objetos são passados para uma classe em vez de serem criados dentro dela. 
Isso promove maior flexibilidade, facilita a manutenção e teste do código, 
permitindo que as dependências sejam facilmente substituídas por outras implementações.

**Problema:**

No exemplo abaixo, a classe Pessoa possui uma forte dependência da classe Casa, resultando em um acoplamento excessivo:

```python
from typing import Type

class Casa:

    def __init__(self) -> None:
        self.__endereco = "Rua A"

    def acender_luzes(self) -> None:
        print("Estou acendendo as luzes...")

    def get_endereco(self) -> str:
        return self.__endereco
    
class Pessoa:

    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

casa_de_amigo = Casa()
ana = Pessoa("Ana", casa_de_amigo)

ana.apresentar_local()
ana.entrar_no_local()
```

Esse acoplamento pode ser resolvido aplicando interfaces e heranças.