from sys import stdin

def QuickSelect(left, right, a, k):
  if (left == right):
    return a[left]
  if(left < right):
    index = left -1
    for j in range(left, right):
      if (a[j] >= a[right]):
        index += 1
        a[index], a[j] = a[j], a[index]
    a[index + 1], a[right] = a[right], a[index + 1]
    index += 1
    if (k == index):
      return a[k]
    if (k < index):
      return QuickSelect(left, index-1, a, k)
    return QuickSelect(index+1, right, a, k)    
 
a = []
n, k = list( [int(i) for i in input().split()] )
for i in range(n):
    a.append(int(stdin.readline()))
  
#print(QuickSelect(0, n-1, a, k-1))
a.sort()
print(a[n - k])