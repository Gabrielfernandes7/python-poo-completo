from interfaces.formas import FormasInterface

class TerrenoQuadrado(FormasInterface):
    def __init__(self, lado: int) -> None:
        self.lado = lado

    def get_perimetro(self) -> int:
        perimetro = self.lado * 4
        return perimetro

    def get_area(self) -> int:
        area = self.lado ** 2
        return area