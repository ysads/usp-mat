import math

def max_dc(A, p, r):
  print(">", p, r)
  if (p == r):
    return A[p]

  q = int(math.floor((p+r)/2))
  x = max_dc(A, p, q)
  y = max_dc(A, q+1, r)

  if (x > y):
    return x
  return y

print("Ex.10.3")
#    0  1  2  3  4  5  6  7  8
A = [1, 3, 5, 4, 8, 2, 9, 0, 7]
print(max_dc(A, 3, 4))
