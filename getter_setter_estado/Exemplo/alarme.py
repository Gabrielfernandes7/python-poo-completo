# getter e setter são mecanismos de acesso aos atributos da minha classe

class Alarme:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado # o estado fica ao encargo de nossa classe
    
    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        self.__estado = valor # por meio do valor alterar meu estado
    