from model import Insersor, Repositorio

repo = Repositorio()
insersor = Insersor(repo)

data = insersor.inserir_dado("Lhama", 26)
print(data)
