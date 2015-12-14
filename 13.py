import re

with open('input/13.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# Organize input
people = {}

for item in input:
  item = re.split(' ', item)
  person = item[0]
  neighbour = item[-1].replace('.', '')
  happiness = int(item[3])
  happiness = -happiness if item[2] == 'lose' else happiness

  if person in people:
    people[person][neighbour] = happiness
  else:
    people[person] = {neighbour: happiness}

def findBestNeighbour(people, person):
  bestNeighbour = {'name': None, 'happiness': None}
  for neighbour, happiness in people[person].iteritems():
    if neighbour not in people: continue
    totalHappiness = people[neighbour][person] + happiness
    if bestNeighbour['happiness'] == None or totalHappiness > bestNeighbour['happiness']:
      bestNeighbour = {'name': neighbour, 'happiness': totalHappiness}
  return bestNeighbour['name']

def findBestArrangment(people, arrangements):
  bestArrangement = {'arrangement': None, 'happiness': None}
  for arrangement in arrangements:
    happiness = 0
    for i in range(len(arrangement)):
      person = arrangement[i]
      neighbour = arrangement[i+1] if i+1 < len(arrangement) else arrangement[0]
      happiness += people[person][neighbour] + people[neighbour][person]
    if bestArrangement['happiness'] == None or happiness > bestArrangement['happiness']:
      bestArrangement = {'arrangement': arrangement, 'happiness': happiness}

  return bestArrangement

# Part 1
print 'Part 1'

# Find best arrangement for each person as start person using greedy algorithm
bestArrangements = []
for person in people:
  bestArrangement = [person]
  peopleCopy = dict(people)
  while len(peopleCopy.keys()) > 1:
    bestNeighbour = findBestNeighbour(peopleCopy, person)
    bestArrangement.append(bestNeighbour)
    del peopleCopy[person]
    person = bestNeighbour
  bestArrangements.append(bestArrangement)

print findBestArrangment(people, bestArrangements)['happiness']

# Part 2
print '\nPart 2'

# Add me to list
people['Leah'] = {}
for person in people:
  if person != 'Leah':
    people['Leah'][person] = 0
    people[person]['Leah'] = 0

# Find best arrangement for each person as start person using greedy algorithm
bestArrangements = []
for person in people:
  bestArrangement = [person]
  peopleCopy = dict(people)
  while len(peopleCopy.keys()) > 1:
    bestNeighbour = findBestNeighbour(peopleCopy, person)
    bestArrangement.append(bestNeighbour)
    del peopleCopy[person]
    person = bestNeighbour
  bestArrangements.append(bestArrangement)

print findBestArrangment(people, bestArrangements)['happiness']


