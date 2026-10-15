def dijkstra(graph, source, destination):
    n = len(graph)
    dist = [9999] * n
    visited = [False] * n
    parent = [-1] * n
    dist[source] = 0
    for _ in range(n):
        u = -1
        min_dist = 9999
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
         if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u
    if dist[destination] == 9999:
        print("No path exists")
        return
    path = []
    v = destination
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
   print("Shortest Path:", end=" ")
    for i in path:
        print(chr(65 + i), end=" ")

    print("\nShortest Distance:", dist[destination])
n = int(input("Enter number of cities: "))
print("Enter adjacency Matrix:")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

source = int(input("Enter Source city: "))
destination = int(input("Enter destination city: "))

dijkstra(graph, source, destination)
