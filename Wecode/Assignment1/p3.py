from sys import stdin, stdout

def TrinarySearch(a, l, r, key, count):
    count += 1
    while l <= r:
        mid1 = l + ((r - l) // 3)
        mid2 = l + (2 * (r - l) // 3) + 1
        if key == a[mid1]:
            return (mid1, count)
        if key == a[mid2]:
            return (mid2, count)
        if key < a[mid1]:
            return TrinarySearch(a, l, mid1 - 1, key, count)
        if key > a[mid2]:
            return TrinarySearch(a, mid2 + 1, r, key, count)
        else:
            return TrinarySearch(a, mid1 + 1, mid2 - 1, key, count)
    return (-1, count)

# input
n = int(stdin.readline())
a = [int(i) for i in stdin.readline().split()]
m = int(stdin.readline())
k = [int(i) for i in stdin.readline().split()]

# main
for i in range(m):
    print(*TrinarySearch(a, 0, n - 1, k[i], 0))