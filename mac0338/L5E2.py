def quocient(n):
    if n == 1:
        return 1

    return 11 * quocient(n-1) + 12

def print_quocient(n):
  print(n, "=>", quocient(n))

print_quocient(n=1)
print_quocient(n=2)
print_quocient(n=3)
print_quocient(n=4)
print_quocient(n=5)
