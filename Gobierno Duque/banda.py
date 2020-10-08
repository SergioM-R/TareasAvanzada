import random

from Bajo import bajo
from guitarra import guitarra
from violin import violin
from musico import musico
from persona import persona

lista = []
lista2 = []
class banda ():
    



    def __init__(self):

        pass

    def agregarmusico(self,nombre):
     
     M = musico()
     M.IngresarNombre(nombre)
     lista.append(M)
     
   

    
    def generarinstrumetno(self):

        r=random.randint(1,3)
        

        if r==1:
            I = bajo("sol")
        elif r==2:
            I=guitarra("sol")
        else:
            I=violin("sol")

        lista2.append(I)
           
    def __str__(self):
        str_con_el_resultado = "Musicos"

        for M in lista:
            str_con_el_resultado += "\n * {}".format(M)
            return str_con_el_resultado


    def PresentarBanda(self):
        
        for M in lista:
            print (M)