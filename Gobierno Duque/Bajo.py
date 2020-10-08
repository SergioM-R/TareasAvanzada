from Instrumentos  import instrumento

class bajo (instrumento):

    def __init__ (self,nota):
        self.nota = nota

    def afinar(self):
        print("afinando bajo")  
    def tocar(self):
        print("tocando bajo")  
    def tocar_nota(self):
        print("tocando bajo con nota", self.nota)