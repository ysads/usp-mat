from math import ceil, floor

def karatsuba(u, v, n):
    if n <= 3:
        return u * v

    m = ceil(n / 2)
    p = floor(u / 10**m)
    q = u % 10**m
    r = floor(v / 10**m)
    s = v % 10**m

    pr = karatsuba(p, r, m)
    qs = karatsuba(q, s, m)
    ps = karatsuba(p, s, m)
    qr = karatsuba(q, r, m)

    uv = pr * 10**(2*m) + (ps + qr) * 10**m + qs

    return uv

print(karatsuba(6514202, 9898989, 7))
