from Instrumentos import instrumento

class violin(instrumento):
    def __init__ (self,nota):
        self.nota =nota

    def afinar (self):
        print("afinando violin")  
    def tocar (self):
        print("tocando violin")  
    def tocar_nota(self):
        print("tocando violin en nota :" + self.nota)