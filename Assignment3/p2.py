def FindKnightTour(tour, m, n):
    if (len(tour) == m*n): 
        print(*tour, sep=" ")
        return True

    move = [(1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (-2, -1), (1, -2), (-1, -2)]
    r = int(tour[len(tour) - 1][1]) - 1
    c = ord(tour[len(tour) - 1][0]) - 97
    exist = False

    for step in move:
        new_r = r + step[0]
        new_c = c + step[1]
        new_pos = chr(new_c + 97) + str(new_r + 1)
        if (new_r >= 0 and new_c >= 0 and new_r < m and new_c < n and new_pos not in tour):
            tour.append(chr(new_c + 97) + str(new_r + 1))
            exist = FindKnightTour(tour, m, n)
            tour.pop()
            if exist: break
    return exist
    
if __name__ == '__main__':
    m, n = [int(i) for i in input().split()]
    start = input()
    tour = [start]
    FindKnightTour(tour, m, n)