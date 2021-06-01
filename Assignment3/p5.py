import heapq
import copy

class Node():
    def __init__(self, state, parent, x, y, cost, level):
        self.state = state
        self.parent = parent
        self.level = level
        self.x = x  # x-pos of zero
        self.y = y  # y-pos of zero
        self.cost = cost

    def __lt__(self, other):
        return self.cost + self.level < other.cost + self.level


row, col = [int(c) for c in input().split()]
ROW = row
COL = col
initial_state = []
goal_state = []
goal_flat = list(range(ROW*COL))
for i in range(ROW):
    vals = [int(i) for i in input().split()]
    initial_state.append(vals)
goal_flat.pop(0)
goal_flat.append(0)
for i in range(ROW):
    r = []
    for j in range(COL):
        r.append(goal_flat[i*COL + j])
    goal_state.append(r)


def calc_cost(state, final):
    count = 0
    for i in range(ROW):
        for j in range(COL):
            if state[i][j] != 0 and state[i][j] != final[i][j]:
                count += 1
    return count


def is_valid(r, c):
    return r >= 0 and c >= 0 and r < ROW and c < COL


def next_state(state, r, c, newr, newc):
    nstate = copy.deepcopy(state)
    nstate[r][c], nstate[newr][newc] = nstate[newr][newc], nstate[r][c]
    return nstate


def find_zero_pos(state):
    for i in range(ROW):
        for j in range(COL):
            if initial_state[i][j] == 0:
                return (j, i)


pq = []
x, y = find_zero_pos(initial_state)
root_cost = calc_cost(initial_state, goal_state)
root = Node(initial_state, None, x, y, root_cost, 0)

heapq.heappush(pq, (root_cost, root))

solution = []
rows = [0, -1, 0, 1]
cols = [1, 0, -1, 0]
solution_found = False
explored = dict()
while not solution_found and len(pq) > 0:
    cost, min = heapq.heappop(pq)

    if min.cost == 0:

        while min.parent is not None:
            solution.append(min.state)
            min = min.parent
        solution.append(min.state)
        solution_found = True
        solution.reverse()
    else:
        explored[str(min.state)] = 1
        for i in range(4):
            next_r = min.y + rows[i]
            next_c = min.x + cols[i]
            if is_valid(next_r, next_c):
                nstate = next_state(min.state, min.y, min.x,
                                    next_r, next_c)
                if str(nstate) not in explored:
                    child_cost = calc_cost(nstate, goal_state)
                    child = Node(nstate, min, next_c, next_r,
                                 child_cost, min.level+1)
                    heapq.heappush(
                        pq, (child_cost + child.level, child))

if solution_found:
    for state in solution:
        for i in range(ROW):
            print(*state[i])
        print('-')