'''
class veicolo():
    def __init__(self, modello, marca, anno, speed):
        print("Creo")
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = speed

    def __str__(self):
        return 'Veicolo: "{} {} {} {}"'.format(self.modello, self.marca, self.anno, self.speed)    
    
    def accelera(self):
        self.speed = self.speed +5
        
    def frena(self):
        self.speed = self.speed -5
        
    def getSPeed(self):
        print(str(self.speed))
        return self.speed
    
class auto(veicolo):
    def __init__(self, modello, marca, anno, speed, numeroPorte):
        super().__init__(modello, marca, anno, speed)
        self.numeroPorte = numeroPorte
        
    def __str__(self):
        return 'Veicolo: "{} {} {} {} {}"'.format(self.modello, self.marca, self.anno, self.speed, self.numeroPorte)
    
class moto(veicolo):
    def __init__(self, modello, marca, anno, speed, tipo):
        super().__init__(modello, marca, anno ,speed)
        self.tipo = tipo
        
    def __str__(self):
        return 'Veicolo: "{} {} {} {} {}"'.format(self.modello, self.marca, self.anno, self.speed, self.tipo)
    
    
#a1 = auto.__init__("Ferrari", "Ferrari", "2000", "2000", "2000")
a1 = auto(modello="dd", marca="Sdd", anno="2334", speed="345", numeroPorte="23")
a1.__str__

'''

class poligono():
    def __init__(self, numLati):
        self.numLati = numLati
        
    def descrizione(self):
        print("Sono un poligono da {} lati".format(self.numLati))
        
class quadrilatero(poligono):
    def __init__(self):
        super().__init__(4)
        
    def descrizione(self):
        print("Sono un quadrilatero")
        
class rettangolo(quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def descrizione(self):
        print("Sono un rettangolo da {} di base e {} di altezza".format(self.base, self.altezza))
        
    def getArea(self):
        return (self.base * self.altezza)
        
    def getPerimetro(self):
        return ((self.base * self.altezza )* 2)
    
class triangolo(poligono):
    def __init__(self, latoA, latoB, latoC):
        super().__init__(3)
        self.a = latoA
        self.b = latoB
        self.c = latoC
        
    def descrizione(self):
        print("Sono un triangolo formato da tre lati di lunghezza {}{}{}".format(self.a, self.b, self.c))
        
    def getPerimetro(self):
        return (self.a + self.b + self.c)
    
    def isEquilatero(self):
        if self.a == self.b == self.c:
            return True
    
        else:
            return False
        
p1 = poligono(4)
q1 = quadrilatero()
r1 = rettangolo(base=5, altezza=6)
t1 = triangolo(5, 6, 7)
#print(str(r1.gePerimetro()))

