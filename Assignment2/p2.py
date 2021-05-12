prime = []

def Sieve_Of_Eratosthenes(n):
    global prime
    isPrime = [True for i in range(n + 1)]
    i = 2
    while(i * i <= n):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
        i += 1
    for i in range(2, n + 1):
        if isPrime[i]: 
            prime.append(i)
    return prime

def Binary_Search(l, r, key):
    global prime
    while(l <= r):
        mid = (l + r) // 2
        if prime[mid] == key: return mid
        if key < prime[mid]: return Binary_Search(l, mid - 1, key)
        return Binary_Search(mid + 1, r, key)
    return -1

even = int(input())
count = 0
prime = Sieve_Of_Eratosthenes(even)
i = 0
while(i < len(prime) and prime[i] < even // 2 + 1):
    if Binary_Search(i, len(prime) - 1, even - prime[i]) != -1:
        count += 1
    i += 1
print(count)