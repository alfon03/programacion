'''
Created on 29 nov 2022

@author: alfon
'''

print("Example: 'Dabale arroz a la zorra el abad', 'anilina', 'Arriba la birra'")
print(",'Logra Casillas allí sacar gol', 'Ligar es ser ágil', 'Líame ese email', '¿Somos o no somos?',")
string = str(input("Enter a phrase: "))
def palindromo(string):
    beginning = 0
    finish = len(string) - 1
    while string[beginning] == string[finish]:
        if beginning >= finish:
            return True
        beginning += 1
        finish -= 1
    return False
def remove_characters(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("á", "a")
    string = string.replace("é", "e")
    string = string.replace("í", "i")
    string = string.replace("ó", "o")
    string = string.replace("ú", "u")
    string = string.replace("?", "¿")
    string = string.replace("¿", "?")
    
    return string

string1 = remove_characters(string)
is_Palindromo = palindromo(string1)

if is_Palindromo:
    print(True)
    print("Is palindromo")
else:
    print(False)
    print("Is not palindromo")
