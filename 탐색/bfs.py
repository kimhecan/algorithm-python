gragh = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []

def bfs(visited, gragh, node):
  #시작노드
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print (s, end=" ")

    for neighbour in gragh[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, gragh, 'A')