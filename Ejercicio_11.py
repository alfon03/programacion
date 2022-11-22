'''
Created on Nov 16, 2022

@author: alfonso
'''
from random import randint

lista = []
lista2 = []
for i in range (6):
    lista.append(randint(0,10))
    lista2.append(randint(0,10))
print(f"Esta es la primera lista:  {lista}")
print(f"Esta es la segunda lista: {lista2}")
res = list(set(lista) & set(lista2))
print(f"Los numeros que tinenen en común (interseción) son: {res}")