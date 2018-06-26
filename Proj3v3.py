#!/bin/python3

import math

# function that takes a number, output a boolean variable
def isPrime(num):
    upperbound = int(math.floor(math.sqrt(num)))
    for i in range(2, upperbound + 1):
        if(num % i == 0):
            return False
    return True


    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # the case where this number is a prime number
    if isPrime(n) is True:
        print(n)
        continue
    
    # clean up all the even factors
    while n % 2 == 0:
        n = n // 2
    
    # check whether it is prime number
    if isPrime(n) is True:
        print(n)
        continue
    
    # if still not prime, factor out all the odd numbers
    primeFlag = False
    
    k = 3
    while k < n+1: 
        if n % k == 0:
            n = n // k
            k = 3
            if isPrime(n) is True:
                print(n)
                primeFlag = True
        else: 
            k = k + 2
        if primeFlag is True:
            break
        

