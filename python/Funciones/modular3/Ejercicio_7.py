'''
Created on 29 nov 2022
@author: alfon
'''
cadena1=("- ¿Nivel de inglés? \n"

"- Alto \n"

"- Bien. Traduzca 'mirar'.\n"

"- Look.\n"

"- Perfecto. Úselo en una frase.\n"

"- 'Luke', yo soy tu padre.\n"

"- Contratado \n")
print(cadena1)
cadena2="Alto"
cadena3="GOD LEVEL"

def reemplazarPalabra(cadena1,cadena2,cadena3):
    nuevafrase=""
    es=0
    desplaza=0
    control=0
    if cadena2 in cadena1:
        c=0
        while c < len(cadena1) and control==0:
            if cadena1[c]==cadena2[0]:
                while es < len(cadena2):
                    if cadena1[c+desplaza]==cadena2[es]:
                        es+=1
                        desplaza+=1
                if es == len(cadena2) and cadena1[c+len(cadena2)]==" ":
                    nuevafrase=nuevafrase + cadena3
                    c+=len(cadena2)
                    es=0
                else:
                    nuevafrase="La palabra a sustituir no se encuentra"
                    es=0
                    c+=1
                    control=1
            else:
                nuevafrase+=cadena1[c]
                c+=1
    return nuevafrase

print(reemplazarPalabra(cadena1,cadena2,cadena3))