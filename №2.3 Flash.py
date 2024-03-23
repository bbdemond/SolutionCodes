k = 0
for x in range(52, 100000, 52):
    if "8" in str(x) and "1" in str(x) and "2" in str(x):
        k+=1
print(k)

