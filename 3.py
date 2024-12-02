def bfs(graph, start):
    queue = [start]
    visited = set([start])

    print('BFS Traversal: ', end=" ")

    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {
    1: [2,3],
    2: [1,4,5],
    3: [1,6],
    4: [2],
    5: [2],
    6: [3]
}

bfs(graph, 1)
