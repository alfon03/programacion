'''
Created on Nov 4, 2022

@author: alfonso
'''

from random import randint

lista = []

for i in range (100+1):
    lista.append(randint(0,1000))
print(f"Estos son los numeros de la lista:  {lista}")
    
def obtenerMayor(lista):
    
    mayor=lista [0]
    
    for i in range (len(lista)):
        if lista [i]>mayor:
            mayor =lista [i]
    #Código
    return mayor

assert (obtenerMayor([1] ) == 1)
print(f"El mayor es: {obtenerMayor(lista)}")

def obtenerMenor(lista):
    
    menor=lista [0]
    
    for i in range (len(lista)):
        if lista [i]<menor:
            menor =lista [i]
    #Código
    return menor

assert (obtenerMenor([1] ) == 1)
print(f"El menor es: {obtenerMenor(lista)}")




def obtenerSuma():
    suma = 0
    
    for i in (lista):
        suma += i

    #Código
    return suma

print(f"La suma de todos los números es: {obtenerSuma()}")

def obtenerMedia ():
    suma = 0
    for i in (lista):
        suma += i
        media = suma / 100
    #Código
    return media

print(f"La media de todos los numeros: {obtenerMedia()}")

def reemplazar_numero ():
    
    n= int(input("Que numero de la lista quieres cambiar: "))
    n2= int(input("Que numero quieres poner: "))
    for i in range (len(lista)):
            
            if n == lista[i]:
                lista[i] = n2   
    return lista
print(f"la sustitucion del numero pedido seria {reemplazar_numero()}")
 

def mostrarTodosNumeros(lista):
    
    print (lista)

print(f"Los numeros son: {lista}")
print("Ha terminado el programa")


