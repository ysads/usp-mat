def f(n):
    if n == 1:
        return 0

    return 2 * f(n / 2) + n


for n in range(0, 5):
    print(n, ">", 2**n, ">", f(2**n))

