# seguindo um diagrama UML

class ControleRemoto:
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self) -> None:
        print("Canal avançado")

    def voltar_canal(self) -> None:
        print("Voltou canal")

    def escolher_canal(self, canal: int) -> None:
        print(f"Você está no canal {canal}")

controleA = ControleRemoto("LG", "Sala")

controleA.avancar_canal()
controleA.escolher_canal(0)