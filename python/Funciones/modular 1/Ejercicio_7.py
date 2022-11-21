'''
Created on Nov 15, 2022

@author: alfonso
'''
"Escribir una función denominada encajan que indique si dos fichas de"
"dominó encajan o no. Las fichas son recibidas en dos cadenas de texto con el"
"siguiente formato [3,4] [2,5]"
from random import randint
lista1 = []
lista2 = []
for i in range (2):
    lista1.append(randint(0,6))
    lista2.append(randint(0,6))
print (lista1, lista2)   

def encaja(lista1, lista2):
    if lista1[0] == lista2[0]:
        return "Encajan las fichas"
    elif lista1[0] == lista2[1]:
        return "Encajan las fichas"
    elif lista1[1] == lista2[0]:
        return "Encaja"
    elif lista1[1] == lista2[1]:
        return "Encajan las dos fichas"
    else:
        return "No encajan ninguna de las fichas"
print(encaja(lista1,lista2))

