from abc import ABC, abstractmethod

class FormasInterface(ABC):
    @abstractmethod
    def get_perimetro(self) -> int:
        pass

    @abstractmethod
    def get_area(self) -> int:
        pass