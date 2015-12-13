import re

input = 'cqjxjnds'

# Part 1
print 'Part 1'

def incrementPassword(password):
  minCharNum = 97
  maxCharNum = 122
  password = list(password)

  for i in range(len(password) - 1, -1, -1):
    charNum = ord(password[i])
    if charNum >= maxCharNum:
      password[i] = chr(minCharNum)
    else:
      password[i] = chr(charNum + 1)
      return ''.join(password)

  return ''.join(password)

def isValidPassword(password):
  rule1Pass = False
  for i in range(3, len(password)):
    if ord(password[i]) == ord(password[i-1]) + 1 and ord(password[i-1]) == ord(password[i-2]) + 1:
      rule1Pass = True

  rule2Pass = not re.search(r'i|o|l', password)

  rule3Pass = sum(1 for element in re.finditer(r'([a-z])\1', password)) >= 2
  return rule1Pass and rule2Pass and rule3Pass

password = incrementPassword(input)
while not isValidPassword(password):
  password = incrementPassword(password)

print password


# Part 2
print '\nPart 2'

password = incrementPassword(password)
while not isValidPassword(password):
  password = incrementPassword(password)

print password