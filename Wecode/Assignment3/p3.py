def MoveDisk(tower, n, src, dst, tmp):
    if n > 0:
        MoveDisk(tower, n - 1, src, tmp, dst)
        # Move n disks from source to destination
        tower[dst].append(tower[src].pop())
        # Print each state of tower after moving disk
        for i in range(3):
            print(*tower[i])
        print("#")
        MoveDisk(tower, n - 1, tmp, dst, src)
    return 

def FindDiskPosition(tower, disk):
    for i in range(3):
        if len(tower[i]) > 0:
            j = len(tower[i]) - 1
            if tower[i][j] == disk: return i, j

def CountSortedDisks(tower, col, disk):
    while disk > 0:
        if (tower[col][disk - 1] - tower[col][disk]) == 1: disk -= 1
        else: break
    return len(tower[col]) - disk

def SolveHanoiTower(tower):
    # Find disk 0 
    c, d = FindDiskPosition(tower, 0)
    n = CountSortedDisks(tower, c, d)
    totalDisks = len(tower[0]) + len(tower[1]) + len(tower[2])
    
    while n < totalDisks:
        # Find unsorted disk from the top of column _c
        _c, _d = FindDiskPosition(tower, n)
        # Specify temporary column
        tmp = [0, 1, 2] 
        tmp.remove(c)
        tmp.remove(_c)
        # Move 1 disk from _c to tmp
        MoveDisk(tower, 1, _c, tmp[0], c)
        d = len(tower[tmp[0]])-1
        # Move n sorted disks from c to tmp
        MoveDisk(tower, n, c, tmp[0], _c)
        c = tmp[0]
        # Update number of sorted disks
        n = CountSortedDisks(tower, c, d)
        
    # Move disk to destination column
    if c != 2:
        tmp = [0, 1, 2]
        tmp.remove(c)
        tmp.remove(2)
        MoveDisk(tower, n, c, 2, tmp[0])

if __name__ == '__main__':
    tower = []
    for i in range(3):
        tower.append([int(i) for i in input().split()])
        # Print first state of tower 
        print(*tower[i])
    print("#")

    SolveHanoiTower(tower)