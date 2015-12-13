import re
import json

with open('input/12.txt', 'r') as f:
  input = f.read()

# Part 1
print 'Part 1'

numbers = re.findall(r'-*[0-9]+', input)
numbers = map(int, numbers)
print sum(numbers)

# Part 2
print '\nPart 2'

inputParsed = json.loads(input)

def processInput(input):
  global result

  if isinstance(input, dict):
    if 'red' in input.values():
      return
    for key, item in input.iteritems():
      processInput(item)
  elif isinstance(input, list):
    for item in input:
      processInput(item)
  elif isinstance(input, int):
    result += input


result = 0
processInput(inputParsed)
print result






