from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangulo
from engenheiro import Engenheiro

engenheiro = Engenheiro("Ana")
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangulo(2, 5)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_perimetro(terrenoRetangular)