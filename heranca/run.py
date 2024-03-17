class Mae:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = "Silva"

    def comer(self) -> None:
        print("Estou comendo !!")
    
    def estudar(self) -> None:
        print("Está estudando")

"""
conseguimos herder os elementos da classe Mae
"""
class Filha(Mae):
    def __init__(self, endereco):
        """
        super() se refere a classe Mae
        __init__() se refere ao construtor da classe Mae
        """
        super().__init__(endereco)

    def brincar(self, brinquedo) -> None:
        print(f"Brincando com {brinquedo}")

ana = Mae("Rua A")
clara = Filha("Rua B")

clara.estudar() # comportamento herdado de mãe

clara.brincar("BONECA")
print(clara.endereco)
