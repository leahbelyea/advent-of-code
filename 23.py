with open('input/23.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

instructions = []

for item in input:
  operation = item[0:3]
  params = item[3:].split(', ')
  params = map(lambda x: x.replace(' ', ''), params)
  instructions.append({'operation': operation, 'params': params})

# Part 1
print 'Part 1'

values = {'a': 0, 'b': 0}
nextInstruction = 0

while nextInstruction < len(instructions):
  instruction = instructions[nextInstruction]
  operation = instruction['operation']
  params = instruction['params']

  if operation == 'hlf':
    values[params[0]] = values[params[0]] / 2
    nextInstruction += 1
  elif operation == 'tpl':
    values[params[0]] = 3 * values[params[0]]
    nextInstruction += 1
  elif operation == 'inc':
    values[params[0]] = values[params[0]] + 1
    nextInstruction += 1
  elif operation == 'jmp':
    nextInstruction += int(params[0])
  elif operation == 'jie':
    if values[params[0]] % 2 == 0:
      nextInstruction += int(params[1])
    else:
      nextInstruction += 1
  elif operation == 'jio':
    if values[params[0]] == 1:
      nextInstruction += int(params[1])
    else:
      nextInstruction += 1

print values['b']

# Part 2
print '\nPart 2'

values = {'a': 1, 'b': 0}
nextInstruction = 0

while nextInstruction < len(instructions):
  instruction = instructions[nextInstruction]
  operation = instruction['operation']
  params = instruction['params']

  if operation == 'hlf':
    values[params[0]] = values[params[0]] / 2
    nextInstruction += 1
  elif operation == 'tpl':
    values[params[0]] = 3 * values[params[0]]
    nextInstruction += 1
  elif operation == 'inc':
    values[params[0]] = values[params[0]] + 1
    nextInstruction += 1
  elif operation == 'jmp':
    nextInstruction += int(params[0])
  elif operation == 'jie':
    if values[params[0]] % 2 == 0:
      nextInstruction += int(params[1])
    else:
      nextInstruction += 1
  elif operation == 'jio':
    if values[params[0]] == 1:
      nextInstruction += int(params[1])
    else:
      nextInstruction += 1

print values['b']

