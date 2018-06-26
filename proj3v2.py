#!/bin/python3

import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # create the original list yet to be filtered
    iniList = list(range(n))
    upperbound = int(math.floor(math.sqrt(n)))
    
    # filter the list
    for i in range(2, upperbound+1):
        iniList = [x for x in iniList if x % i != 0]
        
    # check whether the remaining number are factor of n.
    for a in reversed(iniList):
        if a == 1:
            print(n)
            break
        
        if n % a == 0:
            print(a)
            break
    
