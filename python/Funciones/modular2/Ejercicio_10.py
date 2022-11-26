'''
Created on 26 nov 2022

@author: alfon
'''
n1=int(input("Enter first number:  "))
n2=int(input("Enter second number:  "))
sum1,sum2=1,1
def isFriendNumber(n,s):
    for i in range(2,n):
        if(n % i==0):
            s=s+i
    return s

sum1,sum2=1,1
sum1 = isFriendNumber(n1, sum1)
sum2 = isFriendNumber(n2, sum2)
if((sum1==n2) and (sum2==n1)):
    print(True)
    print("The numbers "+str(n1)+" and "+ str(n2)+" are friendly numbers")

else:
    print(False)
    print("The numbers "+str(n1)+" and "+ str(n2)+" are not friendly numbers")

    