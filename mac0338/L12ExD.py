# ==================
#    POR COLUNAS
#
def print_mat(mat, n, c):
  print("\t", end="")
  for j in range(c+1):
    print(j, "", sep="\t", end="")
  print("\n")
  for i in range(n+1):
    print(i, ">\t", end="")
    for j in range(c+1):
      print(mat[i][j], "\t", end="")
    print("\n")

def subset_sum_prog_din(p, n, c):
  t = [['-' for j in range(c+1)] for i in range(n+1)]

  for i in range(n+1):
    t[i][0] = 1

  for j in range(1, c+1):
    t[0][j] = 0
    for i in range(1, n+1):
      b = t[i-1][j]
      # WARNING! should use `p[i]` upon delivery
      if b == 0 and p[i-1] <= j:
        b = t[i-1][j-p[i-1]]
      t[i][j] = b
    # print_mat(t, n, c)

  print_mat(t, n, c)

  return t[n][c]


# p = [4, 2, 1, 3]
# c = 10
# print(subset_sum_prog_din(p, len(p), c)) # 1

p = [5, 1, 4]
c = 6
print(subset_sum_prog_din(p, len(p), c)) # 0
