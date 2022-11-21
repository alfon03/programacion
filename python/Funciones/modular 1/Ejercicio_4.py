'''
Created on Nov 11, 2022

@author: alfonso
'''
lista=[]
numero = int(input("Introduce un numero:  "))

while numero<0:
    numero = int(input("Introduce un numero:   "))

def obtener_mayor (lista):
    mayor=lista [0]
    
    for i in range (len(lista)):
        if lista [i]>mayor:
            mayor =lista [i]
    
    return mayor

def obtener_pares (lista):
    for i in range (len(lista)):
        if lista [i] % 2 == 0:
            lista.append(numero)
while numero>0:
    if numero >= 0:
        lista.append(numero)
        numero = int(input("Introduce un numero:   "))
        obtener_pares (lista)
        obtener_mayor (lista)
    
print (f"La lista seria {lista}")
print (f"Los pares serian {obtener_mayor}")
            