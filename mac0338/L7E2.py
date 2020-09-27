from math import ceil

def t(n):
    if n == 2:
        return 2

    if n == 3:
        return 3

    return 2 * t(ceil(n/2)) + t(ceil(n/2) + 1) + n

def test(n):
    print(n, "=>", t(n))

for i in range(2,9):
    test(i)
