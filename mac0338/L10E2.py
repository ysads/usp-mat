import math

def print_paths(paths):
  print("=== SSC ===")
  for i in range(len(paths)):
    print("{i:02}: {path}".format(i=i, path=paths[i]))
  print("\n")

def ssdc_max_prog_din(A, n):
  c = [0 for i in range(n)]
  paths = [[A[i]] for i in range(n)]
  
  for m in range(n):
    c[m] = 1
    for i in range(m-1, -1, -1):
      if (A[i] <= A[m]) and (c[i] + 1 > c[m]):
        paths[m] = paths[i] + [A[m]]
        c[m] = c[i] + 1

  # print_paths(paths)

  return c, paths


def ssc_max(A, n):
  c, paths = ssdc_max_prog_din(A, n)
  c_max = 0
  i_max = 0
  print("DP:", c)

  for i in range(n):
    if c[i] > c_max:
      i_max = i
      c_max = c[i]

  return c_max, paths[i_max]
  
print("Ex.10.2")
#     0   1   2   3   4   5   6   7   8   9
# A = [40, 11, 90, 22, 33, 50, 60, 44, 70, 55]
# print("A")
# print(A)
# print("Max SSC: ", ssc_max(A, len(A)))

# B = [32, 19, 32, 17, 31, 43, 30, 29, 54, 16, 28, 52, 15, 41, 65, 14, 50]
# print("\nB")
# print(B)
# print("Max SSC: ", ssc_max(B, len(B)))

C = [80, 22, 78, 30, 65, 41, 12, 70]
print("\nC")
print(C)
print("Max SSC: ", ssc_max(C, len(C)))

D = [57, 16, 10, 34, 91, 45, 19, 45, 22, 51, 23, 48]
print("\nD")
print(D)
print("Max SSC: ", ssc_max(D, len(D)))
