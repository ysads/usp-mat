import itertools

a = [1, 2, 3, 4, 5]
permutations = list(itertools.permutations(a))

count = 0
for p in permutations:
    if p[0] == a[-1]:
        count += 1
    print(p)

print("Pr[X=1]:", count)
