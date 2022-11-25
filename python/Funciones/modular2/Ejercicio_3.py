'''
Created on Nov 22, 2022

@author: alfonso
'''
year=int(input("Enter a year:  "))
month=int(input("Enter a month:  "))
if year <=0 or month <=0 or month>=13:
    def incorrect (year, month):
        return (-1)
    print(incorrect(month, year))
elif year>0 or month >=1 or month <=12:
    def incorrect (month,year):
        if year <=0 or month <=0 or month>=13:
            print(-1)
        print(f"{incorrect (month,year)}")
    def isLeapYear (year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    def computeDaysInMonth (month, year):
        # Abril, junio, septiembre y noviembre tienen 30
        if month in [4, 6, 9, 11]:
            return 30
        # Febrero depende de si es o no bisiesto
        elif month == 2:
            if isLeapYear (year):
                return 29
            else:
                return 28
        else:
            # En caso contrario, tiene 31 días
            return 31
    
    days = computeDaysInMonth (month, year)
    print(f"Para el año {year} y el mes {month} los dias son {days}")
