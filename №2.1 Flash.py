k = 0
for x1 in "0123456789":
    for x2 in "0123456789":
        for x3 in "0123456789":
            for x4 in "0123456789":
                for x5 in "0123456789":
                    n = x1 + x2 + x3 + x4 + x5
                    if (int(n) % 52 == 0 and '8' in n and '1' in n and '2' in n):
                        k += 1
print(k)
                    
