from abc import ABCMeta, abstractmethod
import random


class instrumento (metaclass=ABCMeta):

    def __init__ (self,nota):
        self.nota = nota

    @abstractmethod
    def afinar(self):
        pass
    @abstractmethod
    def tocar(self):
        pass
    @abstractmethod
    def tocar_nota(self): 
        pass


        
