def Count(maze, r, c):
    metzero = False
    for i in range(r):
        if maze[i][0] == 0:
            metzero = True
        if metzero:
            maze[i][0] = 0

    metzero = False
    for i in range(c):
        if maze[0][i] == 0:
            metzero = True
        if metzero:
            maze[0][i] = 0

    if maze[0][0] != 1:
        return 0

    for i in range(1, r):
        for j in range(1, c):
            if maze[i][j] == 0:
                continue
            pr = i - 1
            pc = j - 1
            tmp1 = 0
            tmp2 = 0
            if pr >= 0:
                tmp1 = maze[pr][j]
            if pc >= 0:
                tmp2 = maze[i][pc]
            maze[pr][j] = 0 
            maze[i][j] = tmp1+tmp2
    return maze[r-1][c-1]

r, c = [int(i) for i in input().split()]
maze = []
for i in range(r):
    maze.append([int(i) for i in input().split()])
print(Count(maze, r, c) % (10**13 + 1))