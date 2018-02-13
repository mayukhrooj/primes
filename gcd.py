#!/usr/bin/env python
from expanded_factors import epform 

def gcd (num,num2):
    n1=epform (num)
    n2=epform (num2)
    #print (n1)
    #print (n2)
    GCD = 1
    for i in xrange(0,len(n1)):
        for j in xrange(0,len(n2)):
            if n1[i][0]==n2[j][0]:
                #print(n1[i][0], n2[j][0])
                #print(n1[i][1], n2[j][1])
                z=min(n1[i][1],n2[j][1])
                R=pow (n1[i][0], z)
                #print(R)
                GCD = GCD * R 
    return GCD

if __name__ == "__main__":
    print("GCD of {},{} is {}".format(36,28,gcd (36,28)))
 
