'''
Created on 24 nov 2022

@author: alfon
'''
n=int(input("Enter a number:  "))
def is_prime(n):
    if n<0:
        return None
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True
print(is_prime(n))