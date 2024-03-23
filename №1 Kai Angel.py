from itertools import *
k = 0

for arr in permutations('HEAVYMETAL2', 5):
    s = "".join(arr)
    if "EA" in s or "M2" in s:
        continue
    k += 1
print(k)
