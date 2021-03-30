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


# MOCHILA-PROG-DIN-TABELA (p, v, n, c)
#     para i crescendo de 0 até n
#         t[i, 0] = 0
#     para j crescendo de 1 até c
#         t[0, j] = 0
#         para i crescendo de 1 até n
#             b = t[i-1, j]
#             se p[i] <= j
#                 b = max(b, v[i] + t[i-1, j-p[i]])
#             t[i, j] = b
#     devolva t
#
# MOCHILA-PROG-DIN (p, v, n, c)


def mochila_prog_din_tabela(p, v, n, c):
  # t[i][j] é o valor da solução da instância (p, v, i, j)
  t = [['-' for j in range(c+1)] for i in range(n+1)]

  for i in range(n+1):
    t[i][0] = 0

  for j in range(1, c+1):
    t[0][j] = 0

    for i in range(1, n+1):
      b = t[i-1][j]

      # WARNING! should use `p[i]` upon delivery
      if p[i-1] <= j:
        b = max(b, v[i-1] + t[i-1][j-p[i-1]])

      t[i][j] = b

  return t
  # print_mat(t, n, c)


def mochila_prog_din(p, v, n, c):
  t = mochila_prog_din_tabela(p, v, n, c)
  x = [9 for i in range(n+1)]

  print_mat(t, n, c)

  j = c
  # for i in range(n, 0, -1):
  while j > 0:
    i = n
    while t[i-1][j] != 0:
      x[i] = 0
      i = i - 1
    x[i] = 1
    j = j - p[i-1]

  print([i for i in range(n+1)])

  return x


# Subset-Sum-Prog-Din (p, n, c, t)
  #  1  se t[n, c] = 1
  #  2      j := c
  #  3      para i := n decrescendo até 1
  #  4          se t[i − 1, j] = 1
  #  5              x[i] := 0   ▷ i não pertence a X
  #  6          senão x[i] := 1   ▷ i pertence a X
  #  7           j := j − p[i]
  #  8      devolva x[1 .. n]


# p   1    2    3    4
# p  = [4,   2,   1,   3]
# v  = [500, 400, 300, 450]
# c  = 5
# print(mochila_prog_din(p, v, len(p), c)) # X = {2, 4}; v(X) = 850


# p   1    2    3    4    5
p  = [2,   3,   1,   5,   4]
v  = [400, 450, 500, 300, 200]
c  = 5
print(mochila_prog_din(p, v, len(p), c)) # X = {2, 3}; v(X) = 950
