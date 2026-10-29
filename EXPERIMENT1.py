from collections import deque


# Function to perform BFS
def bfd(graph,start):
  visited = set()
  queue = deque([start])
  visited.add(start)

  print("BFS Traversal:", end=" ")

  while queue:
    vertex = queue.popleft()
    print(vertex,end=" ")

    for neighbor in graph[vertex]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)

#Main Program
graph = {}
n = int(input("Enter the number of vertices: "))

for i in range(n):
  vertex = input(f"Enter vertex {i+1}: ")
  neighbors = input(f"Enter adjacent vertices of {vertex} (space-separated): ").split()
  graph[vertex] = neighbors # Correctly indented inside the loop

start = input("Enter the starting vertex: ")
print("\nGraph:", graph)

bfd(graph,start)