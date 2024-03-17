from interfaces.formas import FormasInterface

class TerrenoRetangulo(FormasInterface):
    def __init__(self, largura: int, comprimento: int) -> None:
        self.largura = largura
        self.comprimento = comprimento

    def get_perimetro(self) -> int:
        perimetro = 2 * ((self.comprimento) + (self.largura))
        return perimetro

    def get_area(self) -> int:
        area = self.comprimento * self.largura
        return area