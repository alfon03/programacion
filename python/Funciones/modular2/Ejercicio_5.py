'''
Created on Nov 22, 2022

@author: alfonso
'''
n1= int(input("Number one (base): ")) 
n2 = int(input("The second number (exponent) : ")or 0) 
def powerIt(n1, n2):
    if( n2 == 0):
        return 1;
    elif n1 == 0:
        return 0
    elif n1<0:
        return n1**n2
    elif n2<0:
        return n2/n1
    
    else:
        return n1* powerIt (n1, n2-1);
print("The operation would be the following: ",n1,"^",n2)
print("The power between the two numbers is:   " + str(powerIt (n1, n2)) );


    
      
    