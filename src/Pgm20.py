
'''
Created on May 28, 2013

@author: Tsss-Pc1
'''
#Program to Check Whether a Number is Prime or Not

n = input()
n=int(n)
m=0
for i in range(n):
    i=i+1
    if n%i==0:
        m=m+1
if m==2:
    print("it is a prime number")
else:
    print("it is not a prime")
        
