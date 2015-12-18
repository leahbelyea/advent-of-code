import itertools

with open('input/17.txt', 'r') as f:
  containers = [int(x.strip('\n')) for x in f.readlines()]

# Part 1
print 'Part 1'

totalVolume = 150
validCombinations = 0

for i in range(1, len(containers) + 1):
  possibleCombinations = itertools.combinations(containers, i)
  for combination in possibleCombinations:
    if sum(combination) == totalVolume:
      validCombinations += 1

print validCombinations

# Part 2
print '\nPart 2'

totalVolume = 150
minNumContainers = None
validCombinations = 0

for i in range(1, len(containers) + 1):
  if minNumContainers != None and i > minNumContainers: break
  possibleCombinations = itertools.combinations(containers, i)
  for combination in possibleCombinations:
    if sum(combination) == totalVolume:
      if minNumContainers == None:
        minNumContainers = i
      validCombinations += 1

print validCombinations