'''
Created on 23 nov 2022

@author: alfon
'''

n1 = int(input("Enter the first number (base number):"))
n2 = int(input("Enter the second number (exponent number):") or 0)

def powerIt(n1, n2=0): 
    if n1<0 or n2<0:
        return (-n1**(n2))
    elif n1 == 0:
        return 0
    elif n2 == 1:
        return  1
    else:
        return (n1**n2)
print(f"The result of raising {n1}^{n2} is {powerIt(n1, n2)}")