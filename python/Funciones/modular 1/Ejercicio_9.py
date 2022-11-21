'''
Created on Nov 18, 2022

@author: alfonso
'''

from random import randint

lista = []

for i in range (10+1):
    lista.append(randint(0,40))
print(f"Estos son los numeros de la lista:  {lista}")
k=int(input("Introduce un número: "))

def menores(k, lista):
    menores = []
    for i in range(len(lista)):
        if lista[i]<k:
            menores.append(lista[i])
    return menores
print(f"Los números menores al número que has introducido son: {menores(k, lista)}")

def mayores(k, lista):
    mayores = []
    for i in range(len(lista)):
        if lista[i]>k:
            mayores.append(lista[i])
    return mayores
print(f"Los números mayores al número introducido son: {mayores(k, lista)}")

def multiplos(k, lista):
    multiplos = []
    for i in range(len(lista)):
        if lista[i]%k==0:
            multiplos.append(lista[i])
    return multiplos
print(f"Los multiplos  del número que se ha introducido son: {multiplos(k, lista)}")
