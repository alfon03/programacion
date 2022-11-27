'''
Created on Nov 18, 2022
@author: alfonso
'''
n=int(input("Enter one number:  "))
def computeFactorial (n):
    if n>=0:
        factorial=1
        for i in range (1,n+1):
            factorial *= i
        return (f"{n}! = {factorial}")
    else:
        return None
print(computeFactorial (n)) 