'''
Created on Nov 9, 2022

@author: alfonso
'''
from random import randint
lista = []

for i in range (10):
    lista.append(randint(0,10))
    

print("Lista desordenada: ", lista)
def estaOrdenada(lista):
    ordenada = True

    for i in range(1,len(lista)):
        if lista[i-1]<lista[i]:
            ordenada=False
    return ordenada
       
print(f"La lista {lista} está ordenada: {estaOrdenada(lista)}")