import re

with open('input/14.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# Definitions
class Reindeer:
  def __init__(self, name, flySpeed, flyTime, restTime):
    self.name = name
    self.flySpeed = int(flySpeed)
    self.flyTime = int(flyTime)
    self.restTime = int(restTime)
    self.atFlightFor = 0
    self.atRestFor = int(restTime)
    self.atRest = True
    self.distance = 0
    self.points = 0

  def __str__(self):
    return '{}: {} km/s for {}s, {}s rest. Distance: {}'.format(self.name, self.flySpeed, self.flyTime, self.restTime, self.distance)

  def doStuff(self):

    if self.atRestFor == self.restTime:
      self.atRestFor = 0
      self.atRest = False
    elif self.atFlightFor == self.flyTime:
      self.atFlightFor = 0
      self.atRest = True

    if self.atRest == True:
      self.atRestFor += 1
    else:
      self.atFlightFor += 1
      self.distance += self.flySpeed

  @staticmethod
  def getWinningReindeer(reindeers):
    maxDistance = 0
    winningReindeer = []
    for reindeer in reindeers:
      if reindeer.distance > maxDistance:
        maxDistance = reindeer.distance

    for reindeer in reindeers:
      if reindeer.distance == maxDistance:
        winningReindeer.append(reindeer)

    return winningReindeer

# Part 1
print 'Part 1'

# Organize input
reindeers = []

for item in input:
  item = re.split(' ', item)
  reindeer = Reindeer(item[0], item[3], item[6], item[13])
  reindeers.append(reindeer)

# Start race
for i in range(2503):
  for reindeer in reindeers:
    reindeer.doStuff()

print Reindeer.getWinningReindeer(reindeers)[0].distance

# Part 2
print '\nPart 2'

# Organize input
reindeers = []

for item in input:
  item = re.split(' ', item)
  reindeer = Reindeer(item[0], item[3], item[6], item[13])
  reindeers.append(reindeer)

# Start race
for i in range(2503):
  for reindeer in reindeers:
    reindeer.doStuff()
  winners = Reindeer.getWinningReindeer(reindeers)
  for winner in winners:
    winner.points += 1

maxPoints = 0
for reindeer in reindeers:
  if reindeer.points > maxPoints:
    maxPoints = reindeer.points

print maxPoints