'''
Created on Nov 17, 2022

@author: alfonso
'''


print("Programa que convierte numero decimal a binario o binario a decimal")
print("Para convertir un número decimal a binario ponga una ,b, al final del número")
print("Para convertir un número binario a decimal ponga una ,d, al final del número")
n =input("Introduce un número que quieras: ")
c=int((n[:-1]))
a=int((n[:-1]))

if "b" in n:
    print(f"Correcto, va a convertir su número {a} decimal a binario")
    
    def convertir_decimal_binario(a):
        numeroBinario = 0
        posicionBinario = 1
        while a != 0:
            numeroBinario = numeroBinario+a%2*posicionBinario
            a//=2
            posicionBinario*=10

            return numeroBinario
    print(convertir_decimal_binario(a))

elif "d" in n:
    for i in range ((c)):
        
        print(f"Correcto, va a convertir su número {c} binario a decimal")
        def convertir_binario_decimal(c): 
            b, i, n = 0, 0, 0
            while(c != 0): 
                a = c % 10
                b = b + a * pow(2, i) 
                c = c//10
                i += 1
            return b
        print(convertir_binario_decimal(c))

        
        print("Incorrecto, no se puede convertir a decimal porque no es un número binario, ya que un número binario se compone de unos y ceros")
elif not "b" or not "d" in n:
    print("Incorrecto, debes poner d o b al final del número")
    



