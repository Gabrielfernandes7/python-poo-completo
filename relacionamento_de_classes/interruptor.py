class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self):
        print(f"Acendendo {self.__comodo}")
    
    def apagar(self):
        print(f"Apagando {self.__comodo}")
