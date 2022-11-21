'''
Created on Nov 16, 2022

@author: alfonso
'''
lista= []
n=int(input("Introduce un número: "))
while n>=0:
    lista.append(n)
    n=int(input("Introduce un número negativo si quieres terminar: "))
    
print(lista)

def sumarNumeros(lista):
    sumatorio = sum(lista)  
    return sumatorio
print(f"La suma de todos los numeros de la lista es: {sumarNumeros(lista)}")

def es_Primo ():
    d=0
    n=0
    a=0
    primos=[]
    while a!=len(lista):
        d=0
        for i in range(1,lista[n]):
            if lista[n]%i==0:
                d = d +1
        
        if d==1:
                primos.append(lista[n])
        n+=1
        a+=1
    return primos
print(f"Los números primos de la lista son:  {es_Primo()}")

def calcularPromedio (lista):
    sumatorio = sum(lista)  
    promedio = sumatorio/(len(lista))
    return promedio
print(f"El valor promedio de la lista es: {calcularPromedio (lista)}")

def calcularFactorial (lista):
    
    for i in range(len(lista)):
        factorial=1
        c = lista[i]
        while(c>1):
            factorial *= c
            c -= 1
        print(f"{lista[i]}! = {factorial}")
    return None
print(calcularFactorial(lista))       
