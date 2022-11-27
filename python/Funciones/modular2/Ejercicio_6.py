'''
Created on 26 nov 2022

@author: alfon
'''
import math
day=int(input("Enter one day: "))
month=int(input("Enter one month: "))
year=int(input("Enter one year: "))
if day <0:
    print("Incorrect")
elif month < 0:
    print("Incorrect")  
elif year < 0:
    print("Incorrect")      

a = (14 - month) / 12
y = year - a
m = month + 12 * a - 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) % 7  

def getDayOfWeek (d):
    if math.trunc(d) >=0:
        if math.trunc(d) == 0:
            return "Monday"
        elif math.trunc(d) == 1:
            return "Tuesday"
        elif math.trunc(d) == 2:
            return "Wenesday"
        elif math.trunc(d) == 3:
            return "Thursday"
        elif math.trunc(d) == 4:
            return "Friday"
        elif math.trunc(d) == 5:
            return "Saturday"
        elif math.trunc(d) == 6:
            return "Sunday"
        else:
            return "Incorrect"
    else:
        return "Incorrect"
print(f"For the day {day}, the month {month} and the year {year}. The date falls on {getDayOfWeek(d)}")
    
