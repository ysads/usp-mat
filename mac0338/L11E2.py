def scd_max_gula(a, b, p, r):
  rr = r-1
  x = [rr]
  k = rr

  for m in range(rr, -1, -1):
    if b[m] < a[k]:
      x.append(m)
      k = m

  return x

a = [1 , 6,  7,  9,  18, 23, 25, 30]
b = [26, 15, 16, 15, 24, 28, 30, 34]

# a = [2, 6,  11, 18, 20, 41]
# b = [8, 10, 16, 37, 39, 43]

scd = scd_max_gula(a, b, 0, len(a))

print("scd:", scd, "\n")
for index in scd:
  print(
    "[{idx}]: {ini}..{fim}".format(idx=index, ini=a[index], fim=b[index])
  )

"""
SCD-Max-Gula (a, b, p, r)
1    X := {r}
2    k := r
3    para m := r-1 decrescendo até 1
4        se b[m] < a[k]
5            X := X ∪ {m}
6            k := m
7    devolva X
"""