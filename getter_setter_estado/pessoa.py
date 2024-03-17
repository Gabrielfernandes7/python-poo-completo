class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print(f"A pessoa está dirigindo um {veiculo}")

    def cantar(self) -> None:
        print("LA LA LA")

    def apresentar_idade(self) -> int:
        return self.idade

pessoaA = Pessoa("Alexandra Elbakyan", 35, "000.000.002")
pessoaB = Pessoa("Ada Lovelace", 209, "000.000.001")

print( f"Nome: {pessoaA.nome} \tIdade: {pessoaA.idade}")
