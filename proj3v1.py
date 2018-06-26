#!/bin/python3

import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    done = False
    isPrime = True
    start = int(math.floor(n / 2))
    while start > 1:
        # first find whether this number is a factor 
        if n % start == 0:
            for i in range(2,int(math.floor(start/2))):
                if start % i == 0:
                    isPrime = False
                    break
            if isPrime is True:
                print(start)
                done = True
                break
        else:
            start = start - 1
        
    # if it does not break and reaches 1, that means the number 
    # itself is a prime number
    if done is False:
        print(n)
