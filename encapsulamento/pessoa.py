# seguindo o UML
# encapsulamento está associado a permissões de uso
# no UML, cpf e apresentar_documentos serão elementos privados

# somente a própria classe poderá ter acesso a classe Pessoa

class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf # para tornar privado: self.__cpf = cpf

    # classe deu acesso ao atributo por meio de um método
    def __apresentar_documento(self): # método privado def __metodo():
        print(self.__cpf)

    def correr(self) -> None:
        print("Pessoa está correndo")

    def beber(self, bebida: str):
        # só apresento o documento em alguma ocasião
        # no caso, quando eu precisar mostrar mostrar mostrar o documento
        # não todo momento
        if bebida == "alcolica":
            self.__apresentar_documento()
        print("Bebendo......")

pessoaA = Pessoa("Alexandra Elbakyan", 35, "000.000.002")
pessoaB = Pessoa("Ada Lovelace", 209, "000.000.001")

print( f"Nome: {pessoaA.nome} \tIdade: {pessoaA.idade}")

pessoaA.beber("alcolica") # mostra o CPF
pessoaB.beber("agua") # não é necessário mostrar o cpf
