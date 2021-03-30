def scd_max_gula(a, b, p, r):
  x = [p]
  k = p

  for m in range(p+1, r):
    if a[m] > b[k]:
      x.append(m)
      k = m

  return x

a = [6,  9,  7,  18, 1,  23, 25, 30]
b = [15, 15, 16, 24, 26, 28, 30, 34]

# a = [2, 06, 11, 18, 20, 41]
# b = [8, 10, 16, 37, 39, 43]

scd = scd_max_gula(a, b, 0, len(a))

print("scd:", scd, "\n")
for index in scd:
  print(
    "[{idx}]: {ini}..{fim}".format(idx=index, ini=a[index], fim=b[index])
  )