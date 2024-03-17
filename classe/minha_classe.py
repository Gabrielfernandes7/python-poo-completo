class MinhaClasse:
    # meu construtor
    def __init__(self, meu_atributo: str, meu_atributo2: str):
        self.meu_atributo = meu_atributo
        self.meu_atributo2 = meu_atributo2

    # esse self indica que esse método pertence a essa classe
    # que se encontra nesse escopo
    def meu_metodo(self) -> None:
        pass

    def meu_metodo2(self, num: int, multi: int) -> int:
        return num * multi

# instanciando minha classe por meio de um objeto
objeto = MinhaClasse("Ola", "Python")
produto = objeto.meu_metodo2(10, 10)

print(objeto.meu_atributo)
print(objeto.meu_atributo2)
print(f"Produdo = {produto}")
