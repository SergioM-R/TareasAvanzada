from Instrumentos import instrumento

class guitarra(instrumento):
    def __init__ (self,nota):
        self.nota =nota

    def afinar (self):
        print("afinando guitarra")  
    def tocar (self):
        print("tocando guitarra")  
    def tocar_nota(self):
        print("tocando guitarra en nota :" + self.nota)
