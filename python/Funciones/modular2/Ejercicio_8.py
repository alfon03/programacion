'''
Created on Nov 24, 2022

@author: alfonso
'''
from math import sqrt
a=int(input("Enter a number for the x²:  "))
b=int(input("Enter a number for the x:  "))
c=int(input("Enter a number for the independent term :  "))

print(f"The equation would be: {a}X² + {b}X + {c}")
def solveSecondOrderEquation(a, b, c):
    solutions = [] 
    discriminating = b * b - 4 * a * c
    if a<0 or b<0 or c<0:
        print("The numbers entered must be positive")
        return None

    if discriminating >= 0: 
        root = sqrt(discriminating)
        solutions.append((-b + root) / (2 * a))   
        if discriminating != 0:
            solutions.append((-b - root) / (2 * a)) 
    else:
        print(f"The discriminant is negative and there are no real solutions of negative square roots: {discriminating} ")
        return None
    return solutions
print(f"The solutions are: {solveSecondOrderEquation(a, b, c)}")