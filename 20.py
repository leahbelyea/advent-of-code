import math

input = 29000000

# Part 1
print 'Part 1'

presentTarget = input
reasonableStartGuess = presentTarget / 50
presentsPerElf = 10

house = reasonableStartGuess

while True:
  presents = 0
  divisors = []
  for i in range(1, int(math.floor(math.sqrt(house))) + 1):
    if house % i == 0:
      divisors.append(i)
  for divisor in divisors:
    presents += divisor * presentsPerElf
    if divisor ** 2 != house:
      presents += (house / divisor) * presentsPerElf
  if presents >= presentTarget: break
  house += 1

print house


# Part 2
print '\nPart 2'

presentTarget = input
presentsPerElf = 11

house =  1
elfVisits = {}
elfLimit = 50

while True:
  presents = 0
  divisors = []
  for i in range(1, int(math.floor(math.sqrt(house))) + 1):
    if house % i == 0:
      divisors.append(i)
  for divisor in divisors:
    if divisor not in elfVisits or elfVisits[divisor] < elfLimit:
      presents += divisor * presentsPerElf
      elfVisits[divisor] = 1 if divisor not in elfVisits else elfVisits[divisor] + 1
    if divisor ** 2 != house:
      if house / divisor not in elfVisits or elfVisits[house / divisor] < elfLimit:
        presents += (house / divisor) * presentsPerElf
        elfVisits[house / divisor] = 1 if house / divisor not in elfVisits else elfVisits[house / divisor] + 1
  if presents >= presentTarget: break
  house += 1

print house
