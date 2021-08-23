def winning(arr, req, max_, max_v):
    memoi = [2*[0] for i in range(req+max_//2)]
    pattern = [["",""] for i in range(req+max_//2)]
    for i in range(-1, len(arr)):
        for j in range(0, req + 2):
            if j <= 0:
                memoi[j][i % 2] = 0
                pattern[j][i%2] = ""
            elif i < 0:
                memoi[j][i % 2] = max_v
            else:
                
                win = memoi[j - arr[i][1]][(i - 1) % 2] + arr[i][2]
                lose = memoi[j][(i - 1) % 2]
                memoi[j][i % 2] = min(win,lose)
                if memoi[j][i % 2] == win:
                    
                    pattern[j][i % 2] = pattern[j - arr[i][1]][(i - 1) % 2] +"." + str(i)
                else:
                    pattern[j][i % 2] = pattern[j][(i - 1) % 2]
                
    x = pattern[req][(len(arr)-1)%2]
    x =x.split('.')
    for i in x:
        if len(i) != 0:
            print(arr[int(i)][0])
    
    
                
    return 
    
n = int(input())
arr = []
win = 0
max_ = 0
max_v = 0
for i in range(n):
    arr.append(list([i for i in input().split()]))
    arr[i][1] = int(arr[i][1])
    win += arr[i][1]
    if max_ < arr[i][1]:
        max_ = arr[i][1]
    arr[i][2] = int(arr[i][2])//2 +1
    max_v += arr[i][2]

(winning(arr, win//2 +1, max_, max_v))