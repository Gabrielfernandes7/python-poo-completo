from abs_class import AbstractClass

class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print("Método abstrato funcionando...")

filha = Filha()
filha.apresentar_metodo()
filha.metodo("Estou aqui")
filha.metodo_abstrato()
