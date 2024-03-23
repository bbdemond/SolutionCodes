from itertools import *
k = 0
for x in product("0123456789", repeat = 5):
    s = "".join(x)
    if int(s) % 52 == 0 and "8" in s and "1" in s and "2" in s:
        k += 1
print(k)
