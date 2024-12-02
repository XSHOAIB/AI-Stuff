def dfs(graph, start):
    stack = [start]
    visited = set()

    print('DFS Traversal: ', end=" ")

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
    
graph = {
    1: [2,3],
    2: [1,4,5],
    3: [1,6],
    4: [2],
    5: [2],
    6: [3]
}

dfs(graph, 1)