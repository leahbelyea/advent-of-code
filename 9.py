import re

with open('input/9.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# Definitions
class Edge:
  def __init__(self, nodes, distance):
    self.nodes = nodes
    self.distance = distance

  def __str__(self):
    return '{} -> {} ({})'.format(self.nodes[0], self.nodes[1], self.distance)

# Build graph
nodes = set()
edges = []

for item in input:
  itemArray = re.split(' to | = ', item)
  itemNodes = itemArray[0:2]
  itemDistance = itemArray[2]
  edges.append(Edge(itemNodes, int(itemDistance)))
  for node in itemNodes:
    nodes.add(node)


# Part 1
print 'Part 1'

def findNearestAdjacentNode(edges, nodes, node):
  potentialEdges = []
  greedyEdge = None
  nextNode = None
  for edge in edges:
    if (node not in edge.nodes): continue
    for edgeNode in edge.nodes:
      if (edgeNode in nodes):
        potentialEdges.append(edge)
  if (len(potentialEdges) == 0): return [0, None]

  for edge in potentialEdges:
    if (greedyEdge == None or edge.distance < greedyEdge.distance):
      greedyEdge = edge
  if (greedyEdge == None): return [0, None]

  for edgeNode in greedyEdge.nodes:
    if edgeNode != node: nextNode = edgeNode
  return [greedyEdge.distance, nextNode]


# Find total distance for every node as start node using greedy algorithm
distances = []
for node in nodes:
  nodesList = list(nodes)
  distance = 0
  nextNode = node

  while (nextNode != None):
    nodesList.remove(nextNode)
    farthestAdjacentNode = findNearestAdjacentNode(edges, nodesList, nextNode)
    distance += farthestAdjacentNode[0]
    nextNode = farthestAdjacentNode[1]

  distances.append(distance)

print min(distances)

# Part 2
print '\nPart 2'

def findFarthestAdjacentNode(edges, nodes, node):
  potentialEdges = []
  greedyEdge = None
  nextNode = None
  for edge in edges:
    if (node not in edge.nodes): continue
    for edgeNode in edge.nodes:
      if (edgeNode in nodes):
        potentialEdges.append(edge)
  if (len(potentialEdges) == 0): return [0, None]

  for edge in potentialEdges:
    if (greedyEdge == None or edge.distance > greedyEdge.distance):
      greedyEdge = edge
  if (greedyEdge == None): return [0, None]

  for edgeNode in greedyEdge.nodes:
    if edgeNode != node: nextNode = edgeNode
  return [greedyEdge.distance, nextNode]

# Build graph
nodes = set()
edges = []

for item in input:
  itemArray = re.split(' to | = ', item)
  itemNodes = itemArray[0:2]
  itemDistance = itemArray[2]
  edges.append(Edge(itemNodes, int(itemDistance)))
  for node in itemNodes:
    nodes.add(node)

# Find total distance for every node as start node using greedy algorithm
distances = []
for node in nodes:
  nodesList = list(nodes)
  distance = 0
  nextNode = node

  while (nextNode != None):
    nodesList.remove(nextNode)
    farthestAdjacentNode = findFarthestAdjacentNode(edges, nodesList, nextNode)
    distance += farthestAdjacentNode[0]
    nextNode = farthestAdjacentNode[1]

  distances.append(distance)

print max(distances)