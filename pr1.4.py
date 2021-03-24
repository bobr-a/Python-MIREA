import math


def f14(n):
    if n == 0:
        return 3
    else:
        return math.cos(f14(n - 1)) + math.tan(f14(n - 1)) + 51

#Makeev
#print(f14(9))
