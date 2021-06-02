def dnc(arr, l, r, visited, cost):
  if (l > r): return 0
  if (l ==  r): return arr[l] * arr[l-1] * arr[l+1]

  m = float('-inf')
  for i in range(l, r + 1):
    left = 0
    right = 0
    if [l, i-1] not in visited:
        left = dnc(arr, l, i-1, visited, cost)
        visited.append([l,i-1])
        cost.append(left)
    else:
        left = cost[visited.index([l,i-1])]
    if [i+1, r] not in visited:
        right = dnc(arr, i+1, r, visited, cost)
        visited.append([i+1,r])
        cost.append(right)
    else:
        right = cost[visited.index([i+1,r])]
    m = max(m, left + right + arr[i]*arr[l-1]*arr[r+1])

  return m

n = int(input())
arr = []
if (n < 20):
  for i in range(n):
    arr.append(int(input()))
arr.append(1)
visited = []
cost = []
print(dnc(arr, 0, n-1, visited, cost))