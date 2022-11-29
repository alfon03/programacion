'''
Created on Nov 29, 2022

@author: alfonso
'''
phrase=input("Enter any phrase: ")

def upperCaseInString():
    return f"Capital Letters: {sum(1 for c in phrase if c.isupper())}"
print(upperCaseInString())