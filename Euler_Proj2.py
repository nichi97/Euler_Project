import sys


t = int(input().strip())


for a0 in range(t):
    n = int(input().strip())
    
    p1 = 1
    p2 = 1

    evenList = []
    switch = 0
    while p1 + p2 <= n : 
        if switch == 0:
            p1 = p1 + p2
            switch = 1
            if p1 % 2 == 0:
                evenList.append(p1)
        else:
            p2 = p1 + p2
            switch = 0
            if p2 % 2 == 0:
                evenList.append(p2)

    print(sum(evenList))
