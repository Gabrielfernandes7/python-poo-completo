# seguindo o UML

class Calculadora:
    def calcular(self, operacao, num1, num2):
        if operacao == "+":
            return self.__adicionar(num1, num2)
        elif operacao == "-":
            return self.__subtrair(num1, num2)
        else:
            return "Operação inválida"

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2
    
calculadora = Calculadora()

resultado = calculadora.calcular("+", 20, 20)

print(resultado)
