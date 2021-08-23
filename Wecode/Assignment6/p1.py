def winning(arr, req, max_):
    memoi = [2*[0] for i in range(req+max_)]
    for i in range(-1, len(arr)):
        for j in range(0, req + 2):
            if j <= 0:
                memoi[j][i % 2] = 0
            elif i < 0:
                memoi[j][i % 2] = float('inf')
            else:
                win = memoi[j - arr[i][1]][(i - 1) % 2] + arr[i][2]
                lose = memoi[j][(i - 1) % 2]
                memoi[j][i % 2] = min(win,lose)
    #print(memoi, req, max_)
    return memoi[req][(len(arr)-1)%2]
    
n = int(input())
arr = []
for i in range(n):
    arr.append(list([i for i in input().split()]))
win = 0
max_ = 0
for i in range(n):
    arr[i][1] = int(arr[i][1])
    win += arr[i][1]
    if max_ < arr[i][1]:
        max_ = arr[i][1]
    arr[i][2] = int(arr[i][2])//2 +1

print(winning(arr, win//2 +1, max_))