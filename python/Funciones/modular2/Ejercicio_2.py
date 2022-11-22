'''
Created on Nov 22, 2022

@author: alfonso
'''
year=int(input("Enter a year:  "))
def isLeapYear (year):
    if not year % 4 and (year % 100 or  not year % 400):
        print("it is leap year")
        return True
    else:
        print("it is not leap year")
        return False
    return None 
print(isLeapYear(year))