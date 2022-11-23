'''
Created on Nov 18, 2022

@author: alfonso
'''
def mostrarNombres(letra, lista):
    lista1 = []
    i=0
    for i in range(len(lista)):
        if lista[i][0]==letra:
            lista1.append(lista[i])
    if len(lista1)==0:
        lista1 = f"No existe ningun nombre en la lista con la letra inicial {letra}"
    return lista1

nombres=["Pedro","Miguel","Jose","Alejandro","Roberto","Pepe","Raquel","Antonio","Juan","Fran","Manuel","Manuel Jesus","Alfonso","Carlos","Francisco José","Iván","Ana","Marta", "Olga", "Tomas", "Tobi"]

letra = input("Introduzca una letra: ").upper()
if letra.isdigit()==True:
    while letra.isdigit()==True:
        letra = input("Por favor, introduzca una letra: ").upper()
print(mostrarNombres(letra, nombres))