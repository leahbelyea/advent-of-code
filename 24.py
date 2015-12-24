import operator
import itertools

with open('input/24.txt', 'r') as f:
  presents = [int(x.strip('\n')) for x in f.readlines()]

def getMinPresentsInFront(presents, groupWeight):
  presents.sort(reverse = True)
  minPresentsInFront = 0
  presentSum = 0
  for present in presents:
    presentSum += present
    minPresentsInFront += 1
    if presentSum >= groupWeight:
      return minPresentsInFront
  return None

def getPossibleGroups(presents, minPresentsInFront):
  possibleGroups = []
  leastPresents = None

  for i in range (minPresentsInFront, len(presents) + 1):
    if leastPresents != None: break
    combinations = itertools.combinations(presents, i)
    for combination in combinations:
      if sum(combination) == groupWeight:
        possibleGroups.append(combination)
        if leastPresents == None or len(combination) < leastPresents:
          leastPresents = len(combination)

  return possibleGroups

# Part 1
print 'Part 1'

totalWeight = sum(presents)
groupWeight = totalWeight / 3

minPresentsInFront = getMinPresentsInFront(presents, groupWeight)
possibleGroups = getPossibleGroups(presents, minPresentsInFront)
possibleGroups = sorted(possibleGroups, key=lambda group: reduce(operator.mul, group, 1))
print reduce(operator.mul, possibleGroups[0], 1)

# Part 2
print '\nPart 2'

totalWeight = sum(presents)
groupWeight = totalWeight / 4


minPresentsInFront = getMinPresentsInFront(presents, groupWeight)
possibleGroups = getPossibleGroups(presents, minPresentsInFront)
possibleGroups = sorted(possibleGroups, key=lambda group: reduce(operator.mul, group, 1))
print reduce(operator.mul, possibleGroups[0], 1)
