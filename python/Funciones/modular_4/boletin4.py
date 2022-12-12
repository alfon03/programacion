'''
Created on 9 dic 2022

@author: alfon
'''
import math
def obtener_menu ():
    def mostrar_menu(eleccion):
        print('Seleccione una opción:')
        for i in sorted(eleccion):
            print(f' {i}) {eleccion[i][0]}')
    
    
    def leer_opcion(eleccion):
        while (a := input('Opción: ')) not in eleccion:
            print('Opción incorrecta, vuelva a intentarlo.')
        return a
    
    
    def ejecutar_opcion(opcion, eleccion):
        eleccion[opcion][1]()
    
    
    def generar_menu(eleccion, opcion_salida):
        opcion = None
        while opcion != opcion_salida:
            mostrar_menu(eleccion)
            opcion = leer_opcion(eleccion)
            ejecutar_opcion(opcion, eleccion)
            print()
    
    
    def menu_principal():
        eleccion = {
            "1": ("usuarios", eleccion1),
            "2": ("Calculo", eleccion2),
            "3": ("Fechas", eleccion3),
            "4": ("Figuras", eleccion4),
            "5": ("Salir", salir)
        }
    
        generar_menu(eleccion, "5")
    
    
    def eleccion1():
        print()
        print("Usuarios")
        print ("Sistema")
        def obtener_menu_usuario ():
            def mostrar_menu_usuario (eleccion_usuario ):
                print("Seleccione una opción:")
                for i in sorted(eleccion_usuario):
                    print(f" {i}) {eleccion_usuario [i][0]}")
            
            
            def leer_opcion_usuario(eleccion_usuario ):
                while (a := input("Opción: ")) not in eleccion_usuario :
                    print("Opción incorrecta, vuelva a intentarlo.")
                return a
            
            
            def ejecutar_opcion_usuario (opcion_usuario, eleccion_usuario):
                eleccion_usuario [opcion_usuario][1]()
            
            
            def generar_menu_usuario (eleccion_usuario , opcion_salida):
                opcion_usuario = None
                while opcion_usuario  != opcion_salida:
                    mostrar_menu_usuario (eleccion_usuario)
                    opcion_usuario= leer_opcion_usuario (eleccion_usuario)
                    ejecutar_opcion_usuario (opcion_usuario, eleccion_usuario)
                    print()
            
            
            def menu_principal_usuario ():
                eleccion_usuario  = {
                    "1": ("Registrarte", eleccion1),
                    "2": ("Iniciar sesion", eleccion2),
                    "3": ("Mostrar usuarios", eleccion3),
                    "4": ("Salir", salir)
                }
            
                generar_menu_usuario (eleccion_usuario , "4")
            
            usuarios={"Alfonso":"34535678"}
            def crear_Usuario(usuario, contraseña, repetir_contraseña,usuarios=usuarios):
                    restrictiones="1234567890^`¨´´';,.-_}{][|@#\ºª¬!·$%&/()=?¿Çç*+ "
                    correcto=0
                    if len(usuarios)==10:
                        correcto=0
                        print("La base de datos esta llena")
                    elif len(contraseña)< 8:
                        correcto=0
                        print("La contraseña tiene que tener almenos 8 caracteres")
                    elif usuario[0] in restrictiones:
                        correcto=0
                        print("El nombre de usuario debe empezar por un caracter alfabetico")
                    elif contraseña!=repetir_contraseña:
                        correcto=0
                        print("La contraseña no coincide")
                    else:
                        correcto=usuarios[usuario]=contraseña
                    return correcto
            def logear(usuario,contraseña,informacion=usuarios):
                correcto=True
                errores=0
                if informacion.get(usuario)=="Bloqueado":
                    print("El cuenta ha sido bloqueada contacte con nosotros por correo o telefono")
                elif usuario in informacion and informacion.get(usuario)!="Bloqueado":
                    while contraseña!=informacion[usuario] and errores <=3:
                        errores+=1
                        contraseña=int(input(f"Introduzca de nuevo su contraseña (Intento {errores}/3):"))
                        if errores >=3:
                            print("El usuario ha quedado bloqueado")
                            informacion[usuario]="Bloqueado"
                            correcto=False
                        if correcto==False:
                            return correcto
                    if informacion[usuario]==contraseña:
                        print("Usted ha accedido al sistema")
                        correcto=True
                            
                else:
                    print("El usuario no existe en nuestra base")
                    correcto=False
                return correcto
            def eleccion1():
                print()
                print("Registrarte")
                if eleccion1 and len(usuarios) <10:
                    usuario=input("Introduzca nombre de usuario deseado: ")
                    contraseña=input("Introduzca contraseña: ")
                    repetir_contraseña=input("Repita la contraseña: ")
                    if usuario in usuarios:
                        print("El usuario ya existe en el sistema")
                    else:
                        while crear_Usuario(usuario,contraseña,repetir_contraseña)==0:
                            usuario=input("Introduzca nombre de usuario deseado: ")
                            contraseña=input("Introduzca la contraseña: ")
                            repetir_contraseña=input("Repita la contraseña: ")
            def eleccion2():
                print()
                print("Iniciar sesion")
                logear(usuario=input("Introduce usuario: \n"), contraseña=input("Introduce contraseña: \n"))

            
            def eleccion3():
                print()
                print("Mostrar ususarios")
                print(usuarios)
                
            def salir():
                print()
                print('Saliendo')
            
            
            if __name__ == "__main__":
                menu_principal_usuario()
            return  "El programa ha terminado"
        print(obtener_menu_usuario())
    
    def eleccion2():
        print()
        print("Calculo")
        def obtener_menu_calculo ():
            def mostrar_menu_calculo(eleccion_calculo):
                print('Seleccione una opción:')
                for i in sorted(eleccion_calculo):
                    print(f' {i}) {eleccion_calculo[i][0]}')
            
            
            def leer_opcion_calculo(eleccion_calculo):
                while (a := input('Opción: ')) not in eleccion_calculo:
                    print('Opción incorrecta, vuelva a intentarlo.')
                return a
            
            
            def ejecutar_opcion_calculo(opcion_calculo, eleccion_calculo):
                eleccion_calculo[opcion_calculo][1]()
            
            
            def generar_menu_calculo(eleccion_calculo, opcion_salida):
                opcion_calculo = None
                while opcion_calculo != opcion_salida:
                    mostrar_menu_calculo(eleccion_calculo)
                    opcion_calculo = leer_opcion_calculo(eleccion_calculo)
                    ejecutar_opcion_calculo(opcion_calculo, eleccion_calculo)
                    print()
            
            
            def menu_principal_calculo():
                eleccion_calculo = {
                    "1": ("Calcular la suma de los digitos de un numero", eleccion1),
                    "2": ("Calcular el maximo comun divisor", eleccion2),
                    "3": ("Calcular el minimo comun un multiplo", eleccion3),
                    "4": ("Programa que acepta dos enteros (n e i) y calcula el valorde n+nn+nnn n....", eleccion4),
                    "5": ("Simplificar fracción:", eleccion5),
                    "6": ("Sumar fracciones:", eleccion6),
                    "7": ("Restar fracciones:", eleccion7),
                    "8": ("Multiplicar fracciones:", eleccion8),
                    "9": ("Dividir fracciones:", eleccion9),
                    "10": ("Salir", salir)
                }
            
                generar_menu_calculo(eleccion_calculo, "10")
            
            
            def eleccion1():
                print()
                print("Calcular la suma de los digitos de un numero")
                n=int(input("Introduce un numero: "))
                tot=0
                while(n>0):
                    dig=n%10
                    tot=tot+dig
                    n=n//10
                print("La suma de lols digitos es:",tot)
            
            def eleccion2():
                print()
                print("Calcular el maximo comun divisor")
                numero=int(input("Introduce un numero: "))
                numero1=int(input("Introduce otro numero: "))
                def mcd(numero, numero1):
                    if(numero1 == 0):
                        return numero
                    else:
                        return mcd(numero1, numero % numero1)
                print(f"El maximo comun divisor de los numeros {numero} y {numero1} es: {mcd(numero, numero1)}")
            
            def eleccion3():
                print()
                print("Calcular el minimo comun un multiplo")
                numero=int(input("Introduce un numero: "))
                numero1=int(input("Introduce otro numero: "))
                def mcd(numero, numero1):
                    if(numero1 == 0):
                        return numero
                    else:
                        return mcd(numero1, numero % numero1)
                def minimo_comun_multiplo(numero, numero1):
                    return (numero*numero1)/int(mcd(numero, numero1))
                print(f"El minimo comun multiplo de los numeros {numero} y {numero1} es: {minimo_comun_multiplo(numero, numero1)}")
            def eleccion4():
                print()
                print("Programa que acepta dos enteros (n e i) y calcula el valorde n+nn+nnn n....")
                numero=int(input("Introduce el primer numero: "))
                numero1=int(input("Introduce el segundo numero: "))
                def sumar_patron(numero, numero1):
                    suma=""
                    for i in range(1,numero1+1):
                        suma+=str(i*numero)
                    return int(suma)
                
                print(sumar_patron(numero, numero1))
            def eleccion5():
                print()
                print("Simplificar fracción")
                numerador=int(input("Introduce el numerador:"))
                denominador=int(input("Introduce el denominador:"))
                print(f"{numerador}/{denominador}")
                def mcd(numerador, denominador):
                    if(denominador == 0):
                        return numerador
                    else:
                        return mcd(denominador, numerador % denominador)
                def simplificar_fraccion(numerador,denominador):
                    numerador=numerador//mcd(numerador,denominador)
                    denominador=denominador//mcd(numerador,denominador)
                    return numerador, denominador
                print(simplificar_fraccion(numerador, denominador))
            
            def eleccion6():
                print()
                print("Sumar fracciones")
                numerador1=int(input("Introduce el numerador:"))
                denominador1=int(input("Introduce el denominador:"))
                print(f"{numerador1}/{denominador1}")
                numerador2=int(input("Introduce el numerador:"))
                denominador2=int(input("Introduce el denominador:"))
                print(f"{numerador2}/{denominador2}")
                
                def sumar_fraccion(numerador1,denominador1,numerador2,denominador2):
                    numerador=(numerador1*denominador2)+(denominador1*numerador2)
                    denominador=denominador1*denominador2
                    def mcd(numerador, denominador):
                        if(denominador == 0):
                            return numerador
                        else:
                            return mcd(denominador, numerador % denominador)
                    def simplificar_fraccion(numerador,denominador):
                        numerador=numerador//mcd(numerador,denominador)
                        denominador=denominador//mcd(numerador,denominador)
                        return numerador, denominador
                    return simplificar_fraccion(numerador,denominador)
                print(sumar_fraccion(numerador1, denominador1, numerador2, denominador2))
                
            def eleccion7():
                print()
                print("Restar fracciones")
                numerador1=int(input("Introduce el numerador:"))
                denominador1=int(input("Introduce el denominador:"))
                print(f"{numerador1}/{denominador1}")
                numerador2=int(input("Introduce el numerador:"))
                denominador2=int(input("Introduce el denominador:"))
                print(f"{numerador2}/{denominador2}")
                
                def restar_fraccion(numerador1,denominador1,numerador2,denominador2):
                    numerador=(numerador1*denominador2)-(denominador1*numerador2)
                    denominador=denominador1*denominador2
                    def mcd(numerador, denominador):
                        if(denominador == 0):
                            return numerador
                        else:
                            return mcd(denominador, numerador % denominador)
                    def simplificar_fraccion(numerador,denominador):
                        numerador=numerador//mcd(numerador,denominador)
                        denominador=denominador//mcd(numerador,denominador)
                        return numerador, denominador
                    return simplificar_fraccion(numerador, denominador)
                print(restar_fraccion(numerador1, denominador1, numerador2, denominador2))
            def eleccion8():
                print()
                print("Multiplicar fracciones")
                numerador1=int(input("Introduce el numerador:"))
                denominador1=int(input("Introduce el denominador:"))
                print(f"{numerador1}/{denominador1}")
                numerador2=int(input("Introduce el numerador:"))
                denominador2=int(input("Introduce el denominador:"))
                print(f"{numerador2}/{denominador2}")
                
                def multiplicar_fraccion(numerador1,denominador1,numerador2,denominador2):
                    numerador=numerador1*denominador1
                    denominador=denominador1*denominador2
                    def mcd(numerador, denominador):
                        if(denominador == 0):
                            return numerador
                        else:
                            return mcd(denominador, numerador % denominador)
                    def simplificar_fraccion(numerador,denominador):
                        numerador=numerador//mcd(numerador,denominador)
                        denominador=denominador//mcd(numerador,denominador)
                        return numerador, denominador
                    return simplificar_fraccion(numerador, denominador)
                print(multiplicar_fraccion(numerador1, denominador1, numerador2, denominador2))
            
            def eleccion9():
                print()
                print("Dividir fracciones")
                numerador1=int(input("Introduce el numerador:"))
                denominador1=int(input("Introduce el denominador:"))
                print(f"{numerador1}/{denominador1}")
                numerador2=int(input("Introduce el numerador:"))
                denominador2=int(input("Introduce el denominador:"))
                print(f"{numerador2}/{denominador2}")  
                def dividir_fraccion(numerador1,denominador1,numerador2,denominador2):
                    numerador=numerador1*denominador2
                    denominador=numerador2*denominador1
                    def mcd(numerador, denominador):
                        if(denominador == 0):
                            return numerador
                        else:
                            return mcd(denominador, numerador % denominador)
                    def simplificar_fraccion(numerador,denominador):
                        numerador=numerador//mcd(numerador,denominador)
                        denominador=denominador//mcd(numerador,denominador)
                        return numerador, denominador
                    return simplificar_fraccion(numerador, denominador)
                print(dividir_fraccion(numerador1, denominador1, numerador2, denominador2))
            def salir():
                print()
                print('Saliendo')
            
            
            if __name__ == '__main__':
                menu_principal_calculo()
            return  "El programa ha terminado"
        print(obtener_menu_calculo())
    
    def eleccion3():
        print()
        print("Fechas")
        def obtener_menu_fechas ():
            def mostrar_menu_fechas (eleccion_fechas ):
                print("Seleccione una opción:")
                for i in sorted(eleccion_fechas):
                    print(f" {i}) {eleccion_fechas [i][0]}")
            
            
            def leer_opcion_fechas(eleccion_fechas ):
                while (a := input("Opción: ")) not in eleccion_fechas :
                    print("Opción incorrecta, vuelva a intentarlo.")
                return a
            
            
            def ejecutar_opcion_fechas (opcion_fechas , eleccion_fechas ):
                eleccion_fechas [opcion_fechas][1]()
            
            
            def generar_menu_fechas (eleccion_fechas , opcion_salida):
                opcion_fechas = None
                while opcion_fechas  != opcion_salida:
                    mostrar_menu_fechas (eleccion_fechas)
                    opcion_fechas= leer_opcion_fechas (eleccion_fechas)
                    ejecutar_opcion_fechas (opcion_fechas, eleccion_fechas)
                    print()
            
            
            def menu_principal_fechas ():
                eleccion_fechas  = {
                    "1": ("Convertir hora/min/segun a segundos", eleccion1),
                    "2": ("Calcular segundos entre dos fechas introducidas", eleccion2),
                    "3": ("Convertir segundos a dia/hora/minutos/segundos", eleccion3),
                    "4": ("Calcular el numero de dias entre dos fechas", eleccion4),
                    "5": ("Programa para imprimir el calendario de un mes y año determinado.", eleccion5),
                    "6": ("Salir", salir)
                }
            
                generar_menu_fechas (eleccion_fechas , "6")
            
            
            def eleccion1():
                print()
                print("Convertir hora/min/segun a segundos")
                def calcular_segundos_dia():
                    print()
                    horas1=int(input("Introduce una hora: "))
                    minutos1=int(input("Introduce los minutos : "))
                    segundos1=int(input("Introduce los segundos: "))
                    print(horas1,":",minutos1,":",segundos1)
                    horas2=int(input("Introduce la hora de este instante: "))
                    minutos2=int(input("Introduce los minutos de este instante: "))
                    segundos2=int(input("Introduce los segundos de este instante: "))
                    print(horas2,":",minutos2,":",segundos2)
                    if horas1<horas2:
                        if horas1==horas2:
                            return 0
                    else:
                        print("Los valores introducidos no son validos la primera hora tiene que ser menor a la que este instante")
                    segundos=(horas2/3600+minutos2/60+segundos2)-(horas1/3600 + minutos1/60 + segundos1)
                    segundos=str(segundos)
                    if "-" in segundos:
                        segundos=segundos[1:]
                    return f"Los segundos entre las dos horas son: {segundos}"
                print(calcular_segundos_dia())
                
            def eleccion2():
                print()
                print("Calcular dias entre dos fechas introducidas")
                def calcular_segundos():
                    segundos = int(input("Introduce el numero de segundos: "))
                    horas =int(input("Introduce el numero de horas: "))
                    minutos = int (input("Introduce el nuemro de minutos: "))
                    
                    segundos1 = int(input("Introduce el numero de segundos: "))
                    horas1 =int(input("Introduce el numero de horas: "))
                    minutos1 = int (input("Introduce el nuemro de minutos: "))
                    
                    if segundos <0 and segundos >60:
                        segundos = int(input("Introduce una cantidad de segundos correcta: "))
                    if segundos1 <0 and segundos1 >60:
                        segundos1 = int(input("Introduce una cantidad de segundos correcta: "))
                    if minutos <0 and minutos >60:
                        minutos = int(input("Introduce una cantidad de minutos correcta: "))
                    if minutos1 <0 and minutos1 >60:
                        minutos1 = int(input("Introduce una cantidad de minutos correcta: "))
                    if horas <0 and horas >24:
                        horas = int(input("Introduce una cantidad de horas correcta: "))
                    if horas1 <0 and horas1 >24:
                        horas1 = int(input("Introduce una cantidad de horas correcta: "))
                    else:
                        print(True)
                    
                    diferencia_segundos = segundos - segundos1
                    diferencia_minutos = minutos - minutos1
                    diferencia_horas= horas - horas1
                    if "-" in str(diferencia_segundos):
                        diferencia_segundos = int(diferencia_segundos)
                        diferencia_segundos = diferencia_segundos[1:]
                    if "-" in str(diferencia_minutos):
                        diferencia_minutos=int(diferencia_minutos)
                        diferencia_minutos = diferencia_minutos[1:]
                    if "-" in str(diferencia_horas):
                        diferencia_horas=int(diferencia_horas)
                        diferencia_horas =diferencia_horas[1:]
                    
                    print(diferencia_horas/diferencia_minutos/diferencia_segundos)
                    
                    diferencia_horas=diferencia_horas*3600
                    diferencia_minutos=diferencia_minutos*60
                    segundos=diferencia_horas+diferencia_minutos+diferencia_segundos
                    resultado=segundos
                    print(resultado)
                print(calcular_segundos())
        
            def eleccion3():
                print()
                print("Convertir segundos a dia/hora/minutos/segundos")
                tiempo = float(input("Introduce un número de segundos: "))
                dia = tiempo // (24 * 3600)
                hora = tiempo // 3600
                tiempo %= 3600
                minutos = tiempo // 60
                tiempo %= 60
                segundos = tiempo
                print("d:h:m:s-> %d:%d:%d:%d" % (dia, hora, minutos, segundos))
            def eleccion4():
                print()
                print("Calcular el numero de dias entre dos fechas")
                def calcular_dias_entre_dos_fechas():
                    year=int(input("Enter a year:  "))
                    day=int(input("Enter a day:  "))
                    month=int(input("Enter a month:  "))
                    if year <=0 or month <=0 or month>=13 or day<=0 or day>=32:
                        def incorrect (year, month, day):
                            return "La fecha introducida es incorrecta"
                        print(incorrect(month, year, day))
                    future_day=(year,month,day)
                    print(future_day)
                    year1=int(input("Enter a year:  "))
                    day1=int(input("Enter a day:  "))
                    month1=int(input("Enter a month:  "))
                    if year1 <=0 or month1 <=0 or month1>=13 or day1<=0 or day1>=32:
                        def incorrect (year, month, day):
                            return "La fecha introducida es incorrecta"
                    future_day1=(year1,month1,day1)
                    print(future_day1)
                    y=year-year1
                    m=month-month1
                    d=day-day1
                    def isLeapYear1 (y):
                        return year % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0)
                    
                    if m in [4, 6, 9, 11]:
                        m=m*30
                    if m == 2:
                        if isLeapYear1 (year1):
                            m=m*29
                        
                        else:
                            m=m*28
                            
                    else:
                        m = m * 31
                    y=y*365
                    resultado= y+m+d
                    resultado=str(resultado)
                    if "-" in resultado:
                        resultado=resultado[1:]
                    return("Los dias entre las dos fechas son:", resultado)
                print(calcular_dias_entre_dos_fechas())
                
            def eleccion5():
                print()
                print("Programa para imprimir el calendario de un mes y año determinado.")
                year = int(input("Input the year : "))
                month = int(input("Input the month : "))
                dias_de_la_semana={0:"Domingo",1:"Lunes",2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado"}
                def calendario_año():
                    def isLeapYear (year1):
                            return year % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0)
                    def getDayOfWeek(day,month,year):
                        if month<1 or year<1:
                            print("Introduzca valores validos")
                        else:
                            a = (14 - month)//12
                            y = year - a
                            m = month + 12 * a - 2
                            d= int(((day + y + y//4 - y//100 + y//400 + (31*m)//12)%7))
                            d=dias_de_la_semana[d]
                        return d
                    
                    def calendar(month,year):
                        calendario=""
                        day=getDayOfWeek(1,month,year)
                        if day=="Lunes" and month==2 and isLeapYear(year)==False:
                            calendario="""
                            L    M    X    J    V    S    D
                            1    2    3    4    5    6    7
                            8    9    10   11   12   13   14
                            15   16   17   18   19   20   21
                            22   23   24   25   26   27   28
                            """        
                        elif day=="Martes" and month==2 and isLeapYear(year)==False:
                            calendario="""
                            L    M    X    J    V    S    D
                                 1    2    3    4    5    6
                            7    8    9    10   11   12   13
                            14   15   16   17   18   19   20
                            21   22   23   24   25   26   27
                            28 
                            """
                        elif day=="Miercoles" and month==2 and isLeapYear(year)==False:
                            calendario="""
                            L    M    X    J    V    S    D
                                      1    2    3    4    5
                            6    7    8    9    10   11   12
                            13   14   15   16   17   18   19
                            20   21   22   23   24   25   26
                            27   28 
                            """
                        elif day=="Jueves" and month==2 and isLeapYear(year)==False:
                            calendario="""
                            L    M    X    J    V    S    D
                                           1    2    3    4
                            5    6    7    8    9    10   11
                            12   13   14   15   16   17   18
                            19   20   21   22   23   24   25
                            26   27   28     
                            """     
                        elif day=="Viernes" and month==2 and isLeapYear(year)==False:
                            calendario="""
                            L    M    X    J    V    S    D
                                                1    2    3
                            4    5    6    7    8    9    10
                            11   12   13   14   15   16   17
                            18   19   20   21   22   23   24
                            25   26   27   28 
                            """             
                        elif day=='Sabado' and month==2 and isLeapYear(year)==False:
                            calendario="""
                            L    M    X    J    V    S    D
                                                     1    2
                            3    4    5    6    7    8    9
                            10   11   12   13   14   15   16
                            17   18   19   20   21   22   23
                            24   25   26   27   28 
                         
                            """
                        elif day=="Domingo" and month==2 and isLeapYear(year)==False:
                            calendario="""
                            L    M    X    J    V    S    D
                                                          1
                            2    3    4    5    6    7    8
                            9    10   11   12   13   14   15
                            16   17   18   19   20   21   22
                            23   24   25   26   27   28   
                            """
                        elif day=="Lunes" and month==2 and isLeapYear(year):
                            calendario="""
                            L    M    X    J    V    S    D
                            1    2    3    4    5    6    7
                            8    9    10   11   12   13   14
                            15   16   17   18   19   20   21
                            22   23   24   25   26   27   28
                            29
                            """        
                        elif day=="Martes" and month==2 and isLeapYear(year):
                            calendario="""
                            L    M    X    J    V    S    D
                                 1    2    3    4    5    6
                            7    8    9    10   11   12   13
                            14   15   16   17   18   19   20
                            21   22   23   24   25   26   27
                            28   29
                            """
                        elif day=="Miercoles" and month==2 and isLeapYear(year):
                            calendario="""
                            L    M    X    J    V    S    D
                                      1    2    3    4    5
                            6    7    8    9    10   11   12
                            13   14   15   16   17   18   19
                            20   21   22   23   24   25   26
                            27   28   29
                            """
                        elif day=="Jueves" and month==2 and isLeapYear(year):
                            calendario="""
                            L    M    X    J    V    S    D
                                           1    2    3    4
                            5    6    7    8    9    10   11
                            12   13   14   15   16   17   18
                            19   20   21   22   23   24   25
                            26   27   28   29  
                            """     
                        elif day=="Viernes" and month==2 and isLeapYear(year):
                            calendario="""
                            L    M    X    J    V    S    D
                                                1    2    3
                            4    5    6    7    8    9    10
                            11   12   13   14   15   16   17
                            18   19   20   21   22   23   24
                            25   26   27   28   29
                            """             
                        elif day=='Sabado' and month==2 and isLeapYear(year):
                            calendario="""
                            L    M    X    J    V    S    D
                                                     1    2
                            3    4    5    6    7    8    9
                            10   11   12   13   14   15   16
                            17   18   19   20   21   22   23
                            24   25   26   27   28   29
                         
                            """
                        elif day=="Domingo" and month==2 and isLeapYear(year):
                            calendario="""
                            L    M    X    J    V    S    D
                                                          1
                            2    3    4    5    6    7    8
                            9    10   11   12   13   14   15
                            16   17   18   19   20   21   22
                            23   24   25   26   27   28   29  
                            """
                        elif day=="Lunes" and (str(month) in "13578" or month == 10 or month==12):
                            calendario="""
                            L    M    X    J    V    S    D
                            1    2    3    4    5    6    7
                            8    9    10   11   12   13   14
                            15   16   17   18   19   20   21
                            22   23   24   25   26   27   28
                            29   30   31
                            """
                        elif day=="Martes" and (str(month) in "13578" or month == 10 or month==12):
                            calendario="""
                            L    M    X    J    V    S    D
                                 1    2    3    4    5    6
                            7    8    9    10   11   12   13
                            14   15   16   17   18   19   20
                            21   22   23   24   25   26   27
                            28   29   30   31
                            """
                        elif day=="Miercoles" and (str(month) in "13578" or month == 10 or month==12):
                            calendario="""
                            L    M    X    J    V    S    D
                                      1    2    3    4    5
                            6    7    8    9    10   11   12
                            13   14   15   16   17   18   19
                            20   21   22   23   24   25   26
                            27   28   29   30   31
                            """
                        elif day=="Jueves" and (str(month) in "13578" or month == 10 or month==12):
                            calendario="""
                            L    M    X    J    V    S    D
                                           1    2    3    4
                            5    6    7    8    9    10   11
                            12   13   14   15   16   17   18
                            19   20   21   22   23   24   25
                            26   27   28   29   30   31    
                            """     
                        elif day=="Viernes" and (str(month) in "13578" or month == 10 or month==12):
                            calendario="""
                            L    M    X    J    V    S    D
                                                1    2    3
                            4    5    6    7    8    9    10
                            11   12   13   14   15   16   17
                            18   19   20   21   22   23   24
                            25   26   27   28   29   30   31
                            """             
                        elif day=='Sabado' and (str(month) in "13578" or month == 10 or month==12):
                            calendario="""
                            L    M    X    J    V    S    D
                                                     1    2
                            3    4    5    6    7    8    9
                            10   11   12   13   14   15   16
                            17   18   19   20   21   22   23
                            24   25   26   27   28   29   30
                            31
                            """
                        elif day=="Domingo" and (str(month) in "13578" or month == 10 or month==12):
                            calendario="""
                            L    M    X    J    V    S    D
                                                          1
                            2    3    4    5    6    7    8
                            9    10   11   12   13   14   15
                            16   17   18   19   20   21   22
                            23   24   25   26   27   28   29
                            30   31
                            """             
                        elif day=="Lunes":
                            calendario="""
                            L    M    X    J    V    S    D
                            1    2    3    4    5    6    7
                            8    9    10   11   12   13   14
                            15   16   17   18   19   20   21
                            22   23   24   25   26   27   28
                            29   30
                            """
                        elif day=="Martes":
                            calendario="""
                            L    M    X    J    V    S    D
                                 1    2    3    4    5    6
                            7    8    9    10   11   12   13
                            14   15   16   17   18   19   20
                            21   22   23   24   25   26   27
                            28   29   30
                            """
                        elif day=="Miercoles":
                            calendario="""
                            L    M    X    J    V    S    D
                                      1    2    3    4    5
                            6    7    8    9    10   11   12
                            13   14   15   16   17   18   19
                            20   21   22   23   24   25   26
                            27   28   29   30
                            """
                        elif day=="Jueves":
                            calendario="""
                            L    M    X    J    V    S    D
                                           1    2    3    4
                            5    6    7    8    9    10   11
                            12   13   14   15   16   17   18
                            19   20   21   22   23   24   25
                            26   27   28   29   30    
                            """     
                        elif day=="Viernes":
                            calendario="""
                            L    M    X    J    V    S    D
                                                1    2    3
                            4    5    6    7    8    9    10
                            11   12   13   14   15   16   17
                            18   19   20   21   22   23   24
                            25   26   27   28   29   30
                            """             
                        elif day=='Sabado':
                            calendario="""
                            L    M    X    J    V    S    D
                                                     1    2
                            3    4    5    6    7    8    9
                            10   11   12   13   14   15   16
                            17   18   19   20   21   22   23
                            24   25   26   27   28   29   30
                         
                            """
                        elif day=="Domingo":
                            calendario="""
                            L    M    X    J    V    S    D
                                                          1
                            2    3    4    5    6    7    8
                            9    10   11   12   13   14   15
                            16   17   18   19   20   21   22
                            23   24   25   26   27   28   29
                            30
                            """             
                        return calendario        
                    print(calendar(month,year))
                print(calendario_año())
            
            def salir():
                print()
                print('Saliendo')
            
            
            if __name__ == "__main__":
                menu_principal_fechas()
            return  "El programa ha terminado"
        print(obtener_menu_fechas ())
    def eleccion4():
        print()
        print("Has elegido la opción 4: figuras")
        def obtener_menu_figuras ():
            def mostrar_menu_figuras(eleccion_figuras):
                print("Seleccione una opción:")
                for i in sorted(eleccion_figuras):
                    print(f" {i}) {eleccion_figuras[i][0]}")
            
            
            def leer_opcion_figuras(eleccion_figuras):
                while (a := input("Opción: ")) not in eleccion_figuras:
                    print("Opción incorrecta, vuelva a intentarlo.")
                return a
            
            
            def ejecutar_opcion_figuras(opcion_figuras, eleccion_figuras):
                eleccion_figuras[opcion_figuras][1]()
            
            
            def generar_menu_figuras(eleccion_figuras, opcion_salida):
                opcion_figuras = None
                while opcion_figuras != opcion_salida:
                    mostrar_menu_figuras(eleccion_figuras)
                    opcion_figuras = leer_opcion_figuras(eleccion_figuras)
                    ejecutar_opcion_figuras(opcion_figuras, eleccion_figuras)
                    print()
            
            
            def menu_principal_figuras():
                eleccion_figuras = {
                    "1": ("Calcular area circulo", eleccion1),
                    "2": ("Calcular diametro circulo", eleccion2),
                    "3": ("Calcular distancia euclídea", eleccion3),
                    "4": ("Calcular perimetro triangulo", eleccion4),
                    "5": ("Calcular area triangulo", eleccion5),
                    "6": ("Salir", salir)
                }
            
                generar_menu_figuras(eleccion_figuras, "6")
            
            
            def eleccion1():
                print()
                print("Calcular area circulo")
                def calcular_area_circulo ():
                    print ("Area Circulo")
                    pi = 3.14
                    
                    radio = int(input("Ingresa el valor del radio: "))
                    area = (radio ** 2) * pi
                    
                    return f"El area es {area}"
                print(calcular_area_circulo())
            
            def eleccion2():
                print()
                print("Calcular diametro circulo")
                def calcular_longitud_circulo():
                    print ("Diametro Circulo")
                    
                    radio = int(input("Ingresa el valor del radio: "))
                    diametro = (radio ** 2)
                    
                    return f"El area es {diametro}"
                print(calcular_longitud_circulo())
            
            def eleccion3():
                print()
                print("Calcular distancia euclídea")
                def calcular_distancia_euclídea():
                    print("ingrese los valores para la coordenada 1")
                    x1 = int(input("ingrese el valor de x1:"))
                    y1 = int(input("ingrese el valor de y1:"))
                    print("ingrese los valores para la coordenada 2")
                    x2 = int(input("ingrese el valor de x2:"))
                    y2 = int(input("ingrese el valor de y2:"))
                    distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
                    return f"la distancia entre la coordenada 1 y la coordenada 2 es = {distancia}"
                print(calcular_distancia_euclídea())
                
            def eleccion4():
                print()
                print("Calcular perimetro triangulo")
                def calcular_perimetro_triangulo():
                    print("Perímetro triángulo")
                    ladoA = float(input("Ingrese el primer lado: "))
                    ladoB = float(input("Ingrese el segundo lado: "))
                    ladoC = float(input("Ingrese el tercer lado: "))
                    perímetro = ladoA + ladoB + ladoC
                    return f"El perimetro del triangulo es {perímetro}"
                print(calcular_perimetro_triangulo())
                
            def eleccion5():
                print()
                print("Calcular area triangulo")
                def calcular_area_triangulo():
                    print()
                    print("Area triángulo")
                    ladoA = int(input("Ingrese el primer lado: "))
                    ladoB = int(input("Ingrese el segundo lado: "))
                    ladoC = int(input("Ingrese el tercer lado: "))
                    perímetro = ladoA + ladoB + ladoC
                    semiperimetro=perímetro/2
                    s=semiperimetro
                    #Formula heron
                    area=s*(s-ladoA)*(s-ladoB)*(s-ladoC)
                    area= math.sqrt(area)
                    return f"El area del triangulo es: {area}"
                print(calcular_area_triangulo())
                
            def salir():
                print()

            
            
            if __name__ == "__main__":
                menu_principal_figuras()
            return  "Saliendo al menu principal"
        print(obtener_menu_figuras())     
    
    def salir():
        print()
        print('Saliendo')
    
    
    if __name__ == '__main__':
        menu_principal()
    return  "El programa ha terminado"
print(obtener_menu())