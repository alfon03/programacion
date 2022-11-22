'''
Created on Nov 16, 2022

@author: alfonso
'''
from random import randint

lista1 = []
lista2 = []
for i in range (6):
    lista1.append(randint(0,10))
    lista2.append(randint(0,10))
print(f"Esta es la primera lista {lista1}")
print(f"Esta es la segunda lista {lista2}")
def unirLista(lista1,lista2):
    fusion=[]
    for i in lista1:
        fusion.append(i)    
    for j in lista2:
        fusion.append(j)
    noRepetir=[]
    for i in fusion:
        if i not in noRepetir:
            noRepetir.append(i)
    return noRepetir

print(f"Esta es la lista común de las dos anteriores listas: {unirLista(lista1, lista2)}")