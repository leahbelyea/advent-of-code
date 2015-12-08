with open('input/7.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
# 'NOT y -> i',
# 'x OR y -> e',
# '123 -> x',
# 'x LSHIFT 2 -> f',
# 'y RSHIFT 2 -> g',
# '456 -> y',
# 'NOT x -> h',
# 'x AND y -> d',
# ]

m16 = 0xffffL

def getNodeValue(label):
  if (label.isdigit()):
    return int(label)
  return int(nodes[label]['value'])

# Make graph
nodes = {}

for edge in input:
  node = {}
  edgeArray = edgeArray = edge.split(' -> ')
  nodeLabel = edgeArray[-1]
  inputArray = edgeArray[0].split(' ')

  if (len(inputArray) == 1):
    if (inputArray[0].isdigit()):
      node['value'] = int(inputArray[0])
    else:
      node['children'] = [inputArray[0]]
  elif (len(inputArray) == 2):
    node['operation'] = 'NOT'
    node['children'] = [inputArray[1]]
  else:
    node['operation'] = inputArray[1]
    node['children'] = [inputArray[0], inputArray[2]]

  nodes[nodeLabel] = node

# Part 1
print 'Part 1'

# Find value of node
nodeToFind = 'a'
while ('value' not in nodes[nodeToFind]) :
  for nodeLabel, node in nodes.iteritems():
    unknownChildren = False
    if ('children' in node):
      for child in node['children']:
        if (not child.isdigit() and 'value' not in nodes[child]):
          unknownChildren = True

      if (not unknownChildren):
        if ('operation' not in node):
          value = getNodeValue(node['children'][0])
        elif (node['operation'] == 'NOT'):
          child1 = getNodeValue(node['children'][0])
          value = int(~(child1) & m16)
        elif (node['operation'] == 'AND'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 & child2
        elif (node['operation'] == 'OR'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 | child2
        elif (node['operation'] == 'LSHIFT'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 << child2
        elif (node['operation'] == 'RSHIFT'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 >> child2

        nodes[nodeLabel]['value'] = value

part1 = nodes[nodeToFind]['value']
print part1

# Part 2
print '\nPart2'

# Reset graph
nodes = {}

for edge in input:
  node = {}
  edgeArray = edgeArray = edge.split(' -> ')
  nodeLabel = edgeArray[-1]
  inputArray = edgeArray[0].split(' ')

  if (len(inputArray) == 1):
    if (inputArray[0].isdigit()):
      node['value'] = int(inputArray[0])
    else:
      node['children'] = [inputArray[0]]
  elif (len(inputArray) == 2):
    node['operation'] = 'NOT'
    node['children'] = [inputArray[1]]
  else:
    node['operation'] = inputArray[1]
    node['children'] = [inputArray[0], inputArray[2]]

  nodes[nodeLabel] = node

# Override b
nodes['b']['value'] = part1

# Find value of node
nodeToFind = 'a'
while ('value' not in nodes[nodeToFind]) :
  for nodeLabel, node in nodes.iteritems():
    unknownChildren = False
    if ('children' in node):
      for child in node['children']:
        if (not child.isdigit() and 'value' not in nodes[child]):
          unknownChildren = True

      if (not unknownChildren):
        if ('operation' not in node):
          value = getNodeValue(node['children'][0])
        elif (node['operation'] == 'NOT'):
          child1 = getNodeValue(node['children'][0])
          value = int(~(child1) & m16)
        elif (node['operation'] == 'AND'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 & child2
        elif (node['operation'] == 'OR'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 | child2
        elif (node['operation'] == 'LSHIFT'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 << child2
        elif (node['operation'] == 'RSHIFT'):
          child1 = getNodeValue(node['children'][0])
          child2 = getNodeValue(node['children'][1])
          value = child1 >> child2

        nodes[nodeLabel]['value'] = value

part2 = nodes[nodeToFind]['value']
print part2









