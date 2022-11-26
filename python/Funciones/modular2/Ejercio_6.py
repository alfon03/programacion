'''
Created on 26 nov 2022

@author: alfon
'''
import time
print("This program tells you how many digits have octal, hexadecimal, decimal and real numbers")
def getNumberOfDigits():   
    time.sleep(0.5)
    n=int(input("Enter a positive or negative number integer:  "))
    def contar_real(n):
        if n<0:
            return f"The number {n} have {len(str(n))-1} digits"  
        elif n>=0:      
            return f"The number {n} have {len(str(n))} digits"
    print(contar_real(n))
    
    n=float(input("Enter a decimal number:  "))
    def contar_decimal(n):
        time.sleep(0.5)
        n = str(n)
        length = len(n)
        i=-1
        leave = False 
        while leave == False:
            i = i + 1
            if n [i] == "." or (length -1 == i):
                leave = True 
                if length -1 == i:
                    i = i + 1
        print("To the left of the point is",i," digits")
        if length ==i:
            print("To the right of the decimal point is 0 digits")
        else:
            print("To the right of the decimal point is", length - i -1, "digits")
        
        total =i + (length - i -1)
        
        return f"In total there are {total} digits"
    print(contar_decimal(n))
    
    
    n=int(input("Enter a number to convert to hexadecimal:  "))
    def obtener_caracter_hexadecimal(n):
        time.sleep(0.5)
        print(f"The number entered {n} will be converted to Hexadecimal")
        valor = str(n)
        equivalencias = {
            "10": "a",
            "11": "b",
            "12": "c",
            "13": "d",
            "14": "e",
            "15": "f",
        }
        if valor in equivalencias:
            print(f"The digits are: {equivalencias[valor]}")
            return f"The digits are: {len(equivalencias[valor])}"
        else:
            print(f"The same number is printed {valor}")
            valor =int(valor)
            if valor<0:
                return f"The digits are: {len(str(valor))-1}"  
            else:      
                return f"The digits are: {len(str(valor))}"
    print(obtener_caracter_hexadecimal(n))
    
    n=int(input("Enter a number to convert to octal:  "))
    
    def decimal_a_octal(n):
        time.sleep(0.5)
        print(f"The number entered {n} will be converted to octal")
        octal = ""
        if n <= 0:
            print("There are no negative octal numbers")
            return None
        while n > 0:
            residue = n % 8
            octal = str(residue) + octal
            n = int(n / 8)
        return f"The digits of this octal number {octal} are: {len(str(octal))}"
    print(decimal_a_octal(n))
    
    n=int(input("Enter a number to convert to binary:  "))
    
    def decimal_a_binario(n):
        time.sleep(0.5)
        print(f"The entered number {n} it will be converted to binary")
        if n <= 0:
            print("There are no negative binary numbers")
            return None
        binario = ""
        while n > 0:
            residue = int(n % 2)
           
            n = int(n / 2)
            
            binario = str(residue) + binario
        return f"The digits of this binary number {binario} are: {len(str(binario))}"
    print(decimal_a_binario(n))
print(getNumberOfDigits())
    
