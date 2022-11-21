'''
Created on Nov 11, 2022

@author: alfonso
'''
dia=int(input("Introduce un dia:  "))
mes=int(input("Introduce un mes:  "))
año=int(input("Introduce un año:  "))



def es_bisiesto (año):
    return (año%4==0 and (año%100!=0 or año%400 == 0))
def es_fecha_valida (d, m, a):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    return (1<= d <= dias[m-1] or (es_bisiesto(a) and m == 2 and 1 <= d <= 29))
       
def transformar_fecha (dia, mes, año):
    meses= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Otubre", "Noviembre", "Diciembre"]
    if es_fecha_valida(transformar_fecha(dia, mes, año)): 
        mes_largo = meses [mes-1]
        resultado = f"{dia} de {mes_largo} de {año}"
    else:
        resultado = "La fecha introducida es incorrecta."
    return resultado
        
    print(resultado)
    
    dia=int(input("Introduce un dia:  "))
    mes=int(input("Introduce un mes:  "))
    año=int(input("Introduce un año:  "))
    while dia >0:
        print(transformar_fecha(dia, mes, año))
        dia=int(input("Introduce un dia:  "))
        mes=int(input("Introduce un mes:  "))
        año=int(input("Introduce un año:  "))
        
    print(resultado)