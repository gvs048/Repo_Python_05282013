
'''
Created on May 28, 2013

@author: Tsss-Pc1
'''
#Program to Count Number of Digits of an Integer

n=input()
n=int(n)
l=1
for i in range(n):
    if int(n/10)==0:
        #print(n,"is single digit")
        break
    else:
        n=n/10
        l=l+1;
        #print("more than one digit")
        #print(l,"digits")
print(l,"digits")