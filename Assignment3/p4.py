def FindGoalState(tower):
    goal = []
    for i in range(3):
        for j in range(len(tower[i])):
            goal.append(tower[i][j])
    goal.sort()
    goal.reverse()
    return goal

def FindMissingDisk(tower, goal):
    if not tower[2]: return goal[0]
    for i in range(len(tower[2]) - 1):
        if tower[2][i] != goal[i]: return goal[i]
    if len(tower[2]) < len(goal): 
        return goal[len(tower[2])]

def FindDiskPosition(tower, diskValue):
    for i in range(3):
        for j in range(len(tower[i])): 
            if tower[i][j] == diskValue:
                return i, j

def CanBeMoved(tower, col, disk):
    return len(tower[col]) - 1 - disk

def CanBePut(tower, goal):
    if not tower[2]: return 0
    for i in range(len(tower[2])):
        if tower[2][i] != goal[i]: return len(tower[2]) - i
    return 0

def MoveDisk(tower, n, src, dst):
    if n > 0:
        MoveDisk(tower, n - 1, src, dst)
        # Move n disks from source to destination
        tower[dst].append(tower[src].pop())
        # Print each state of tower after moving disk
        for i in range(3):
            print(*tower[i])
        print("#")
    return 

def SolveEzRuleTower(tower):
    goal = FindGoalState(tower)

    while len(tower[2]) < len(goal):
        c, d = FindDiskPosition(tower, FindMissingDisk(tower, goal))

        tmp = [0, 1]
        # Number of disks on top of a column need to be moved before moving needed disk
        n = CanBeMoved(tower, c, d)
        # Number of disks need to be moved before putting right disk into dest col
        m = CanBePut(tower, goal)
        # print("========\n", "n, m", n, m, "\n========")
        if c == 2:
            if n != 0: MoveDisk(tower, n, 2, 0)
            MoveDisk(tower, 1, 2, 0)
            if m != 0: MoveDisk(tower, m, 2, 1)
            MoveDisk(tower, 1, 0, 2) 
        else:
            tmp.remove(c)
            if m == 0: 
                if n != 0: 
                    MoveDisk(tower, n, c, tmp[0])
                MoveDisk(tower, 1, c, 2)
            else: 
                if n != 0:
                    MoveDisk(tower, n, c, tmp[0])
                MoveDisk(tower, 1, c, tmp[0])
                MoveDisk(tower, m, 2, c)
                MoveDisk(tower, 1, tmp[0], 2)
                

if __name__ == '__main__':
    tower = []
    for i in range(3):
        tower.append([int(i) for i in input().split()])
        # Print first state of tower 
        print(*tower[i])
    print("#")

    SolveEzRuleTower(tower)