from datetime import datetime


dizionario  = {}
        
letto = open('data.csv', 'r')  
for riga in letto:
    #print(riga)
    lista = riga.split(",")
    
    if lista[0] != "date" and lista[1] != "passengers" and lista[1] != "\n":
        data = lista[0].split("-")
        passeggeri = int(lista[1])

        #print(lista[0])
        #print(lista[1])
        
        
        if not data[0] in dizionario.keys():
            dizionario[data[0]] = [passeggeri]
        else:
            dizionario[data[0]].append(passeggeri)
        
        
letto.close()
#print(dizionario)
'''
medie = []
for chiave in dizionario.keys():
    b = dizionario[chiave]
    #print(b)
    somma = sum(b)
print(chiave + ": =" + str(round(somma / len(b), 2)))
medie.append([chiave, round(somma / len(b), 2)])
'''


class CSVTimeSeriesFile():
    def __init__(self, nome):
        self.nome = nome
        
    def getData(self):
        ris = []
        letto = open('data.csv', 'r')
        for riga in letto:
            lista = riga.split(",")
        
            if lista[0] != "date" and lista[1] != "passengers" and lista[1] != "\n":
                passeggeri = int(lista[1])
                ris.append([lista[0], passeggeri])
        return ris
    
    def getSomma(self, anno):
        b = dizionario[anno]
        somma = sum(b)
        return somma
    
    def getMedie(self):
        medie = []
        for chiave in dizionario.keys():
            b = dizionario[chiave]
            somma = sum(b)
            if not chiave in medie.keys():
                medie[chiave] = [str(round(somma / len(b), 2))]
            else:
                medie[chiave].append(str(round(somma / len(b), 2)))
        return medie

def computer_var(vet, primo, ultimo):
    print("In fase di costruzione")
    
    
    
    
    
A = CSVTimeSeriesFile("data.csv")
b = A.getData()
print(b)
computer_var(b, "1952", "1955")
m = A.getMedie()