from itertools import *
k = 0
for n in range(100000, 1000000):
    f = True
    for arr in permutations('174', 2):
        s = "".join(arr)
        if s in str(n):
            f = False
    for arr in permutations('226', 2):
        s = "".join(arr)
        if s in str(n):
            f = False
    if f:
        k += 1
print(k, int((k/900000) * 100))
