'''
Created on 24 nov 2022

@author: alfon
'''
import time
print("This program makes you enter a number and then tells you its divisors. \n")
print("Then it prints you a list with the divisors and proceeds to tell you if the numbers are prime or not. \n")
print("Finally, the program tells you the divisors that are prime. \n")
n=int(input("Enter one number:  "))
lista2=[]
lista1=[]
def getDivisors (n):
    contador = 0
    print("The divisors of",n,"are")
    if n<0:
        return None
    for getDivisors in range(1,n+1):
       
        if n%getDivisors==0 :
            print(getDivisors,"is divisor")
            time.sleep(0.5)
            contador += 1
            lista1.append(getDivisors)
    print("This is the list of divisors", lista1)
    return f"The number {n} have {contador} divisors"
print(getDivisors(n))
def is_Prime(n):
    divisor = 0
    if n >=0:
        for i in range(1, n):
            if n % i ==0:
                divisor +=1
    if divisor == 1:
        print(f"The number {n} is prime")
        return True
    else:
        print(f"The number {n} ins't prime")
        return False
print(is_Prime(n))

def getPrineDivisors (n):
    for i in range(2, n+1):
        if n%i==0 and is_Prime(i)==True:
            lista2.append(i)
    return lista2
print(f"The prime divisors of {n} are {getPrineDivisors(n)}")