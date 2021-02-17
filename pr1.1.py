import math


def f11(x, y, z):

    return math.fabs(z) - y - 39 / z ** 4 - y - 10 - (57 * z ** 7 - y ** 8) - math.sqrt(math.exp(z) + y - 37)


#print('%.2e' % f11(-27, -10, 39))
