'''
def contaParola(parola):
    conta = 0
    with open("./../esercizi/testo.txt", "r") as testo:
        for riga in testo:
            par = riga.strip("\n")
            if par == parola:
                conta = conta + 1
    return conta
                
print(contaParola("clown"))
'''
'''
def contaParole(nomeFile):
    dizionario = {}
    with open("./../esercizi/" + nomeFile, "r") as testo:
        for riga in testo:
            parola = riga.strip("\n")
            if not parola in dizionario.keys():
                dizionario[parola] = 1
            else:
                dizionario[parola] = dizionario[parola] + 1
    return dizionario

print(contaParole("testo.txt"))
'''
'''
def contaLunghezze(nomeFile):
    dizionario = {}
    with open("./../esercizi/" + nomeFile, "r") as testo:
        for riga in testo:
            parola = riga.strip("\n")
            carattere = parola[0]
            print(carattere)
            if not carattere in dizionario.keys():
                dizionario[carattere] = parola
            else:
                if len(dizionario[carattere]) <= len(parola):
                    dizionario[carattere] = parola
    return dizionario
                
print(contaLunghezze("testo.txt"))
'''
'''
nomeFile = "./../esercizi/testo.txt"

class ExamException(Exception):
    pass

try:
    testo = open(nomeFile, "r")
    testo.close()
except:
    raise ExamException("NOn va")

d = 0
print("Adesso ci siamo")
print(d)
'''