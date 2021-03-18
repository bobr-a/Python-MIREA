import math


def f12(x):
    if x < 20:
        return x ** 8 - 84 * x ** 2 - 40
    elif 20 <= x < 96:
        return math.exp(x ** 2) + math.log1p(x)
    elif 96 <= x < 195:
        return x ** 5 + x ** 7 - 63
    elif 195 <= x < 207:
        return x ** 4 - math.log1p(x) + 12 * x ** 4
    elif x >= 207:
        return (math.sin(x) - x ** 8 - 7) ** 7 - 17 * x ** 3

#Makeev
print('%.2e' % f12(-24))
