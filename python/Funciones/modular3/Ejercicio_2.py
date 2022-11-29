'''
Created on Nov 29, 2022

@author: alfonso
'''
phrase=input("Enter any phrase: ")
def lowCaseInString():
    return f"Lowercase Letters:  {sum(1 for c in phrase if c.islower())}"
print(lowCaseInString())