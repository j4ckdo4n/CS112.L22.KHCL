import heapq

graph = dict()
visited = set()
vertex = set()

def FindPath(path, step, index, src, dest, cost, totalVertex):
    global graph, visited

    if (index == totalVertex):
        for i in graph[src]:
            w, v = i
            totalCost = w + cost
            if v == dest:
                step[index] = dest
                heapq.heappush(path, (totalCost, step[:]))
                step[index] = ''
                return
        return

    for i in graph[src]:
        w, v = i
        if v not in visited:
            visited.add(v)
            step[index] = v
            FindPath(path, step, index + 1, v, dest, cost + w, totalVertex)
            visited.remove(v)
            step[index] = ''

if __name__ == '__main__':
    # Initialize input 
    n, start = input().split()
    for i in range(int(n)):
        u, v, w = input().split()
        w = int(w)
        vertex.add(u)
        vertex.add(v)

        if (u in graph):
            heapq.heappush(graph[u], (w, v))
        else:
            graph[u] = [(w, v)]

    visited.add(start)
    step = ['' for i in range(len(vertex) + 1)]
    step[0] = start
    path = []

    # Processing
    FindPath(path, step, 1, start, start, 0, len(vertex))
    if len(path) > 0:
        w, minPath = heapq.heappop(path)
        print(*minPath)
