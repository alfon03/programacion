'''
Created on Nov 29, 2022

@author: alfonso
'''
string=str(input("Enter a phrase you want:"))
def contar_vocales(string):
    contador = 0
    for letter in string:
        if letter.lower() in "aeiou":
            contador += 1
    return contador

amount = contar_vocales(string)
print(f"In the chain '{string}' have {amount} vowels")
