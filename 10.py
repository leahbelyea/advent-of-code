import re

input = '1113222113'

# Part 1
print 'Part 1'

for i in range(0, 40):
  components = re.finditer(r'([1-9])\1*', input)
  input = ''
  for component in components:
    digit = component.group()[0]
    numDigits = len(component.group())
    input += '{}{}'.format(numDigits, digit)

print len(input)

# Part 2
print '\nPart 2'

for i in range(0, 10):
  components = re.finditer(r'([1-9])\1*', input)
  input = ''
  for component in components:
    digit = component.group()[0]
    numDigits = len(component.group())
    input += '{}{}'.format(numDigits, digit)

print len(input)