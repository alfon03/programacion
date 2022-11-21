'''
Created on Nov 8, 2022

@author: alfonso
'''

lista = ["Di", "buen", "día", "a", "papa"]

def invertir(lista):
    lista2=[]
    for i in range(len(lista)):
        lista2.append(lista[(i+1)*-1])
    return lista2
print(invertir(lista))
