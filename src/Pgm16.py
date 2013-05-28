
'''
Created on May 28, 2013

@author: Tsss-Pc1
'''
#Program to Display Fibonacci Series



# Import the system library. This allows us to access stdin later.
import sys

# Here's our main function. Python is pretty efficient here. You
# should notice that there are no braces. Python is dependant on
# whitespace to define blocks.

def main():
    print( "\nHow many numbers of the sequence would you like?")
    n = int(sys.stdin.readline())
    fibonacci(n)

# Here's the fibonacci function. Like in Perl, you can assign multiple
# variables on a line without using a temporary variable. Also, the for 
# loop here works more like a foreach loop by setting a range from 0 to n.

def fibonacci(n):
    a,b = 0,1
    for i in range(0,n):
        print(a)
        #print a
        a,b, = b,a+b

main()
input('Press<enter>')

