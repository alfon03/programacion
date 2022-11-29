'''
Created on 29 nov 2022

@author: alfon
'''
text=str(input("Enter a text or phrase: "))
def contar_palabras():
    result = len(text.split())
    return "There are " + str(result) + " words."
print(contar_palabras())