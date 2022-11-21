'''
Created on Nov 10, 2022

@author: alfonso
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
def desplazar_derecha(lista, desplazamiento = 1):
    a_borrar, a_escribir = 0, lista [0]
    for i in range(len(lista)):
        a_borrar = lista[(i+ desplazamiento)%len(lista)]
        lista[(i + desplazamiento)%len(lista)] = a_escribir
        a_escribir = a_borrar
        
    return lista
print(desplazar_derecha(lista))