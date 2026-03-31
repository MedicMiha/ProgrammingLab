class MovingAvarage():
    def __init__(self, dim):
        if not type(dim) == int:
            raise ExamException("Dim data non intera")
        self.dim = dim
        
        self.vet = []
        self.somma = 0
        self.medie = []
        
    def compute(self, lista):
        print("ciao")
        
        if not type(lista) == list or not all(isinstance(x, int) for x in lista):
            raise ExamException("Lista non di numeri")
            
        if self.dim >= len(lista):
            raise ExamException("finestra troppo grande")
        
        y = 0
        while y < len(lista) - self.dim +1:
            self.somma = 0
            x = 0
            self.vet = []
            while x < self.dim:
                print(str(x))
                self.vet.append(lista[y+x])
                x = x+1
            y = y+1
            i = 0
            while i < self.dim:
                self.somma = self.somma + self.vet[i]
                i = i+1
            self.medie.append(self.somma / self.dim)
        print(self.medie)
        return self.medie
        
    def getDim(self):
        return self.dim
           
class ExamException(Exception):
    pass


lista = [2,34,6,8,14]
A = MovingAvarage(2)
b = A.compute(lista)