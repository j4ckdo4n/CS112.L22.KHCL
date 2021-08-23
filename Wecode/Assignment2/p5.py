combination = []

def Generate(pair, left, right, n):
    global combination
    if len(pair) == 2 * n:
        combination.append(pair)
        return
    if left < n:
        Generate(pair + '(', left + 1, right, n) 
    if right < left:
        Generate(pair + ')', left, right + 1, n) 
        
n = int(input())
Generate('', 0, 0, n)
print(*combination, sep = '\n')