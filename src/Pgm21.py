
'''
Created on May 28, 2013

@author: Tsss-Pc1
'''
#Program to Display Prime Numbers Between Two Intervals

n = input()
n=int(n)

m = input()
m=int(m)

p=0
for j in range(n,m):
    for i in range(j):
        i=i+1
        if j%i==0:
            p=p+1
    if p==2:
        print(j,"it is a prime number")
    #else:
        #print(j,"it is not a prime")
    p=0  
