print("Ciao")

'''
tot = 538
i = 0
while tot > 60:
    tot = tot - 60
    i = i + 1
print(str(i) + "h:" + str(tot) + "min")
'''
#----------------------------------------------------
'''
num = -1
while num <= -1 or num >= 20:
    num = int(input("Inserisci un numero tra 0 e 20: "))
'''
'''
print("Il suo quadrato è: " + str(num**2))
print("Il suo cubo è: " + str(num**3))
#----------------------------------------------------
num = int(input("Inserisci un numero: "))
if num % 2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")
'''
#----------------------------------------------------
'''
def conta(parola, lettera):

    i = parola.count(lettera)
    print("Numeri: " + str(i))
    

lettera = input("Inserisci lettera:")
parola = input("Inserisci Parola")
conta(parola, lettera)
'''
#----------------------------------------------------
'''
def ePrimo(num):
    i=2
    primo = True
    while i < num:
        if num % i == 0:
            primo = False
        i = i+1
    
    if primo == True:
        print("Primo")
    else:
        print("Non primo")
        
ePrimo(num)
'''
#----------------------------------------------
'''
num = -1
sum = 0
while num != 0:
    num = int(input("Inserisci un numero diverso da 0: "))
    sum = sum + num

print(str(sum))
'''
#----------------------------------------------
'''
def fattoriale(numero):
    
    i = numero
    fat = 1
    while i >= 1:
    
        fat = fat * i
        i=i-1
    return fat

num = 5
fatt = fattoriale(num)
print(str(fatt))
'''
#-------------------------------------------------
'''
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))
num3 = int(input("Inserisci il terzo numero: "))

def triangolo(num1, num2, num3):
    print("Entra")
    if num1 == num2 == num3:
        print("Triangolo Equilatero")
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print("Triangolo Isoscele")
    else:
        print("Triangolo Scaleno")
'''
#----------------------------------------------
'''
vocali = ['a', 'e', 'i', 'o', 'u']
parola = input("Inserisci parola: ")

def contaVoc(parola):
    conta = 0
    #print(parola)
    x = 0
    while x < len(parola):
        i = 0
        while i < 5:
            #print("voc:"+ vocali[i])
            #print("char:" + parola[x])
            if vocali[i] == parola[x]:
                conta = conta + 1
            i =i+1
        x=x+1
    return conta


d = contaVoc(parola)
print(str(d))
'''
