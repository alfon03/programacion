'''
Created on 24 nov 2022

@author: alfon
'''
n1=int(input("Enter one number:"))
n2=int(input("Enter second number:"))
def isFriendNumber ():
    
    def suma(n1,n2):
    
        for i in range(2,n1):
            if(n1 % i==0):
                    n2=n2+i
        return n2
    def check(suma):
        sum1,sum2=1,1
        sum1 = suma(n1, sum1)
        sum2 = suma(n2, sum2)
        if((sum1==n2) and (sum2==n1)):
            #return True
            print("The numbers "+str(n1)+" and "+
            str(n2)+" are friendly numbers.")
        else:
            #return False
            print("The numbers "+str(n1)+" and "+ 
            str(n2)+" are not friendly numbers.")
print(isFriendNumber())