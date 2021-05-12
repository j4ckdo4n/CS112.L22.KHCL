n = int(input())
quantity = 9e+9
count = 0

for a in range(n // 500000 + 1):
    for b in range((n - a * 500000) // 200000 + 1):
        for c in range(((n - a * 500000) - b * 200000) // 100000 + 1):
            for d in range((((n - a * 500000) - b * 200000) - c * 100000) // 50000 + 1):
                for e in range(((((n - a * 500000) - b * 200000) - c * 100000) - d * 50000) // 20000 + 1):
                    if a * 500000 + b * 200000 + c * 100000 + d * 50000 + e * 20000 == n:
                        count += 1
                        temp = a + b + c + d + e
                        if(quantity > temp): quantity = temp    

if(count == 0): print(0, 0)
else: print(count, quantity)