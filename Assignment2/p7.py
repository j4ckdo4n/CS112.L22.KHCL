def GenerateScore(arr, score, pos, sum, GPA, ans, posAns):
  if (pos == len(arr)):
    if (round(sum+0.001, 1) == GPA):
      print(*ans, sep = ' ')
    return

  for i in score:
    if (i - int(i) == 0):
      ans[pos] = int(i)
    else:
      ans[pos] = i

    nextsum = sum + ans[pos] * arr[pos]
    newPosAns = posAns + arr[pos]

    if round(nextsum +  10*(1-newPosAns) + 0.001, 1) < GPA or round(nextsum + 0.25*(1-newPosAns)+ 0.001, 1) > GPA:
      continue
    else:
      GenerateScore(arr, score, pos+1, nextsum, GPA, ans, newPosAns)



arr = []
n = int(input())
for i in range(n):
  arr.append(int(input()) / 100)
GPA = float(input())

score = [i / 100 for i in range(25, 1025, 25)]
ans = [0 for i in range(n)]

#Print result
GenerateScore(arr, score, 0, 0, GPA, ans, 0)