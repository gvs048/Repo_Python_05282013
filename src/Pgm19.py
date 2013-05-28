
'''
Created on May 28, 2013

@author: Tsss-Pc1
'''
#Program to know palindrome or not

n = input()
n=int(n)
m=n
num=''

while int(n) != 0 :
    num=num+str(n%10)
    n=int(n/10)
print(num)

if m==int(num):
    print("palindrome")
else:
    print("not a palindrome")
    

