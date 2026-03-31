#1
'''
numeri = []
insert = 1

while insert >= 1:
    insert = int(input("Inserisci num: "))
    if insert%2 != 0 and insert != 0:
        numeri.append(insert)
        
print(numeri)
'''
#2
'''
lista = [[1,2,3],[4,5,6], [7,8,9]]

for x in lista:
    for y in x:
        print(y)
'''
#3
'''
lista1 = [1,2,3,4,5,6,8,9]
lista2 = [2,3,4,5,6]
lista12 = []

for x in lista1:
    for y in lista2:
        if x*y > 10:
            lista12.append(x*y)
'''
#4
'''
def tripla(x, y, z):
    if x**2 + y**2 == z**2 and x != y and x != z and y != z:
        print("terna pitgorica")
        return True
    return False
        
        
a = 1
b = 2
c = 3
conta = 0

for a in range(20):
    for b in range(20):
        for c in range(20):
            if tripla(a, b, c) == True:
                conta = conta + 1
                print(a , b, c)
#oppure
#lista  = [{a, b,c} for a in range(20) for b in range(20), for c in range(20) if tripla(a, b, c) == True]


print(conta)
'''
#5
'''
lista1 = [0, 1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd', 'e']

lista3 = [{a, b} for a in lista1 for j, b in enumerate(lista2) if a%2 == 0 and j%2 != 0]
print(lista3)
'''
#6
'''
frase = "the cat sat on the mat the cat"
dizionario = {}

lista = frase.split(" ")
for x in lista:
    if x in dizionario:
        dizionario[x] = dizionario[x] + 1
    else:
        dizionario[x] = 1

print(dizionario)

# questoinvece è dict comprehension
frase = "the cat sat on the mat the cat"
lista = frase.split()
dizionario = {parola: lista.count(parola) for parola in lista}
print(dizionario)

'''
