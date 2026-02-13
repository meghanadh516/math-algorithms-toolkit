# algorithms/graph.py

graph = {}

def add_vertex(v):
    if v not in graph:
        graph[v] = []

def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def print_graph():
    for vertex, edges in graph.items():
        print(f"{vertex}: {edges}")

# Traversals

""" BFS (Breadth-first search) """

from collections import deque

def bfs(start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend([v for v in graph[vertex] if v not in visited])

""" DFS(Depth-First Search) """

def dfs(start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)

