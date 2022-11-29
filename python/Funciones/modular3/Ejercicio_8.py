'''
Created on 29 nov 2022

@author: alfon
'''
string=str(input("Enter a phrase you want:"))
def contar_vocales(string):
    contador = []
    for letter in string:
        if letter.lower() in "aeiou"  and letter.lower() not in contador:
            contador += letter
    return len (contador)

amount = contar_vocales(string)
print(f"In the chain '{string}' have {amount} vowels")