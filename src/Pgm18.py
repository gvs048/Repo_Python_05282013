
'''
Created on May 28, 2013

@author: Tsss-Pc1
'''
#Program to Reverse a Number

n = input()
n=int(n)
num=''

while int(n) != 0 :
    num=num+str(n%10)
    n=int(n/10)
print(num)


