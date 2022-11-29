'''
Created on 29 nov 2022

@author: alfon
'''
phrase = str(input("Enter a phrase: "))
vowels = 'aeiou'
consonants = "qwrtyplñkjhgfdszxcvbnm"
a = ""
b= ""
for x in phrase:
    if x in vowels:
        a += x
    elif x in consonants:
        b +=x 
print(f"The change is:",b+a)