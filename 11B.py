from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = int(input("Enter vertex: "))
    graph[vertex] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph[u].append(v)
    graph[v].append(u)   

print("\nGraph:")
for vertex in graph:
    print(vertex, "->", graph[vertex])



def bfs(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return result



def dfs(start):
    visited = set()
    result = []

    def visit(node):
        visited.add(node)
        result.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return result


start = int(input("\nEnter starting vertex: "))

print("BFS:", bfs(start))
print("DFS:", dfs(start))
