with open('input/6.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = ['turn on 0,0 through 999,999']
# input = ['toggle 0,0 through 999,0']
# input = ['turn off 499,499 through 500,500']

# Part 1
print 'Part 1'
lightGrid = [[0 for x in range(1000)] for x in range(1000)]

for instruction in input:
  instructionArray = instruction.split(' ');
  instructionType = instructionArray[0] if instructionArray[0] == 'toggle' else instructionArray[1]
  startPoint = [int(n) for n in instructionArray[-3].split(',')]
  endPoint = [int(n) for n in instructionArray[-1].split(',')]

  for i in range (startPoint[0], endPoint[0] + 1):
    for j in range  (startPoint[1], endPoint[1] + 1):
      if instructionType == 'on':
        lightGrid[i][j] = 1
      elif instructionType == 'off':
        lightGrid[i][j] = 0
      elif instructionType == 'toggle':
        if (lightGrid[i][j] == 0): lightGrid[i][j] = 1
        elif (lightGrid[i][j] == 1): lightGrid[i][j] = 0

numLightsOn = 0
for array in lightGrid:
  numLightsOn += sum(array)

print numLightsOn

# Part 2
print '\nPart 2'
lightGrid = [[0 for x in range(1000)] for x in range(1000)]

for instruction in input:
  instructionArray = instruction.split(' ');
  instructionType = instructionArray[0] if instructionArray[0] == 'toggle' else instructionArray[1]
  startPoint = [int(n) for n in instructionArray[-3].split(',')]
  endPoint = [int(n) for n in instructionArray[-1].split(',')]

  for i in range (startPoint[0], endPoint[0] + 1):
    for j in range  (startPoint[1], endPoint[1] + 1):
      if instructionType == 'on':
        lightGrid[i][j] += 1
      elif instructionType == 'off':
        if lightGrid[i][j] > 0: lightGrid[i][j] -= 1
      elif instructionType == 'toggle':
        lightGrid[i][j] += 2

brightness = 0
for array in lightGrid:
  brightness += sum(array)

print brightness





