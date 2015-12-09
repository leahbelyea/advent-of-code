import re
import json

with open('input/8.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# Part 1
print 'Part 1'

codeLength = 0
memoryLength = 0

for string in input:
	rawString = string
	decodedString = rawString.decode('string_escape')
	codeLength += len(rawString)
	memoryLength += len(decodedString) - 2 # minus 2 for start and end quotes

print codeLength - memoryLength

# Part 2
print '\nPart 2'

codeLength = 0
memoryLength = 0

for string in input:
	rawString = string
	encodedString = json.dumps(rawString)
	codeLength += len(rawString)
	memoryLength += len(encodedString)

print memoryLength - codeLength
