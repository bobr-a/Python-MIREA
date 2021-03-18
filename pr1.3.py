def f13(n, m):
    s1 = 0
    s2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s1 += j ** 8 - 84 * j ** 2 - 40
    for i in range(1, n + 1):
        s2 += 69 * i + i ** 5
    s2 = 66* s2
    return s1 - s2

#Makeev
#print('%.2e' % f13(63, 77))
