with open('input/18.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# Part 1
print 'Part 1'

class LightDisplay:
  def __init__(self, grid, part):
    self.grid = grid
    self.part = part

  def __str__(self):
    gridString = ''
    for row in self.grid:
      gridString += ('').join(map(str, row)).replace('1', '#').replace('0', '.') + '\n'
    return gridString

  def doStep(self):
    newGrid = [[0 for x in range(len(self.grid))] for x in range(len(self.grid))]
    for row in range(len(self.grid)):
      for column in range(len(self.grid)):
        numNeighboursOn = self.getNeighboursOn(row, column)
        if self.grid[row][column] == 1 and numNeighboursOn in [2, 3]:
          newGrid[row][column] = 1
        elif self.grid[row][column] == 0 and numNeighboursOn == 3:
          newGrid[row][column] = 1
        elif self.part == 2 and self.isAlwaysOn(row, column):
          newGrid[row][column] = 1
    self.grid = newGrid

  def getNeighboursOn(self, row, column):
    neighbours = []
    for x in range(row-1, row+2):
      for y in range(column-1, column+2):
        if x >= 0 and y>= 0 and x < len(self.grid) and y < len(self.grid) and not (x == row and y == column):
          neighbours.append(self.grid[x][y])
    return sum(neighbours)

  def getLightsOn(self):
    numLightsOn = 0
    for row in self.grid:
      numLightsOn += sum(row)
    return numLightsOn

  def isAlwaysOn(self, row, column):
    if row == 0 and column == 0:
      return True
    elif row == 0 and column == len(self.grid) - 1:
      return True
    elif row == len(self.grid) - 1 and column == len(self.grid) - 1:
      return True
    elif row == len(self.grid) - 1 and column == 0:
      return True
    return False

  def turnCornersOn(self):
    self.grid[0][0] = 1
    self.grid[0][len(self.grid) - 1] = 1
    self.grid[len(self.grid) - 1][0] = 1
    self.grid[len(self.grid) - 1][len(self.grid) - 1] = 1

grid = []
for line in input:
  line = list(line.replace('#', '1').replace('.', '0'))
  grid.append(map(int, line))

display = LightDisplay(grid, 1)
for i in range(100):
  display.doStep()

print display.getLightsOn()

# Part 2
print '\nPart 2'

grid = []
for line in input:
  line = list(line.replace('#', '1').replace('.', '0'))
  grid.append(map(int, line))

display = LightDisplay(grid, 2)
display.turnCornersOn()

for i in range(100):
  display.doStep()

print display.getLightsOn()

