def FindWords(matrix, s, i, j, index):
    if len(s) == index: 
        return True
    if (i < 0) or (i >= len(matrix)) or (j < 0) or (j >= len(matrix[0])) or (index > len(s)):
        return False  
    if matrix[i][j] != s[index]: 
        return False 

    matrix[i][j] = ''
    words = FindWords(matrix, s, i - 1, j, index + 1)
    words = words or FindWords(matrix, s, i + 1, j, index + 1)
    words = words or FindWords(matrix, s, i, j - 1, index + 1)  
    words = words or FindWords(matrix, s, i, j + 1, index + 1)
    words = words or FindWords(matrix, s, i - 1, j - 1, index + 1)
    words = words or FindWords(matrix, s, i - 1, j + 1, index + 1)
    words = words or FindWords(matrix, s, i + 1, j - 1, index + 1)
    words = words or FindWords(matrix, s, i + 1, j + 1, index + 1)
    matrix[i][j] = s[index]
    return words

def PrintWords(matrix, s):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if FindWords(matrix, s, i, j, 0): 
                print("true")
                return
    print("false") 

# input
s = input()
matrix = []
while True:
    c = input()
    if(c == "."): break
    tmp = []
    for i in c:
        tmp.append(i)
    matrix.append(tmp)
PrintWords(matrix, s)