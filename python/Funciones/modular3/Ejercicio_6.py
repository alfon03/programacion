'''
Created on 29 nov 2022

@author: alfon
'''
import time
print("Hay una palabra esconcida en la siguiente texto")
print("")
frase="Según_estudios_realizados_por_la_universidad_inglesa_de_cambridge"
texto="aasdSgeglúen_egstjugdliñogs_raeañloieziaodjogs_pgohr_lka_uinaivfenrsdigdgahd_ajinkgñlehsa_dfe_claomybvrnimd.g´e"
time.sleep(2)
print("")
print(texto)
def buscarPalabra(frase,texto):
    time.sleep(5)
    buscar=""
    posicion=0
    contiene=False
    for c in texto:
        if c == frase[posicion]:
            buscar+=c
            posicion+=1
    if buscar==frase:
        contiene=True
    
    return contiene
print(buscarPalabra(frase,texto))
print("")
print(f"Esta es la frase: {frase}")
print("")


#El siguiente codigo es otro ejemplo para que podamos ver que el codigo tambien puede darnos False como queriamos


print("Hay una palabra esconcida en el siguiente texto")
print("")
frase="hola"
texto="soybahxlna"
time.sleep(2)
print("")
print(texto)
def buscarPalabra2(frase,texto):
    time.sleep(5)
    buscar=""
    posicion=0
    contiene=False
    for c in texto:
        if c == frase[posicion]:
            buscar+=c
            posicion+=1
    if buscar==frase:
        contiene=True
    
    return contiene
print(buscarPalabra2(frase,texto))
print("")
print(f"Esta es la palabra que queriamos buscar: {frase}, pero no se encuentra en el texto.")
print("")

#Este de aqui es otro ejemplo mas

print("Hay una palabra esconcida en la siguiente texto")
print("")
frase="hola"
texto="shybaoxlna"
time.sleep(2)
print(texto)
print("")
def buscarPalabra3(frase,texto):
    time.sleep(5)
    buscar=""
    posicion=0
    contiene=False
    for c in texto:
        if c == frase[posicion]:
            buscar+=c
            posicion+=1
    if buscar==frase:
        contiene=True
    
    return contiene
print(buscarPalabra3(frase,texto))
print("")
print(f"Esta es la frase: {frase}")




