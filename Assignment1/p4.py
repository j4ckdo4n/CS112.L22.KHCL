from sys import stdin, stdout

t = int(input())
while(t > 0):
    n, m = [int(i) for i in stdin.readline().split()]
    a = [int(i) for i in stdin.readline().split()]
    b = [int(i) for i in stdin.readline().split()]
    arr = a + b
    arr.sort()
    if (len(arr) % 2) == 0:
        ans = arr[(len(arr) - 1) // 2] + arr[(len(arr) - 1) // 2 + 1]
        if (ans % 2) == 0:
            print(ans // 2)
        else:
            print(ans / 2)
    else:
        print(arr[(len(arr) - 1) // 2])
    t -= 1