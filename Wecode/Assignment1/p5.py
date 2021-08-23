from sys import stdin, stdout

t = int(input())
while(t > 0):
    try:
        n, m, k = [int(i) for i in stdin.readline().split()]
        a = [int(i) for i in stdin.readline().split()]
        b = [int(i) for i in stdin.readline().split()]
        arr = a + b
        arr.sort()
        stdout.write(str(arr[k]) + '\n')
    except:
        continue
    t -= 1