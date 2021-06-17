def Count(x):
    c = [2, 5, 10, 20, 50]
    f = [1e9] * (x + 1)

    for i in range(2, x + 1):
        if (i in c): f[i] = 1
        else:
            tmp = [f[i - j] for j in c if (i - j) >= 0]
            f[i] = min([i for i in tmp if (i != 0)]) + 1

    if f[x] == 1e9:
        return 0
    return f[x]

    
n = int(input())
print(Count(n // 10000))