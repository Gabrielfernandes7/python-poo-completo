from interruptor import Interruptor
from typing import Type

class Pessoa:
    # estou afirmando que meu Interruptor é um tipo
    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self):
        print("Dormindo...")