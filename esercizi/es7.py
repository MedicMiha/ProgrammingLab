from datetime import datetime

'''
data = 0
while TRUE:
    try:
        data = datetime(input("Inserisci data: "))
    except:
        pass

'''
#6
'''
num = 'A'

while type(num) != int:
    try:
        num = int(input("Inserisci: "))
    except:
        pass

print(str(num**2))
'''
#7
'''
num = 0

def menu():
    print("1) Somma due numeri")
    print("2) Sottrai due numeri")
    print("3) Esci")
    try:
        return int(input("Scegli"))
    except:
        raise Exception("Errore Stringa - Intero")
        

def somma(A, B):
    print(str(A+B))
    return (A+B)

def sottrai(C, D):
    print(str(C-D))
    return (C-D)

while num != 3:
    num = menu()
    if num == 1:
        try:
            a = int(input("Primo numero"))
            b = int(input("Secondo numero"))
        except:
            raise Exception("Errore Stringa - Intero")
        somma(a, b)
    elif num == 2:
        try:
            c = int(input("Primo numero"))
            d = int(input("Secondo numero"))
        except:
            raise Exception("Errore Stringa - Intero")
        sottrai(c, d)
    else:
        print("Comando non riconosciuto.")
    
'''