import re

with open('input/5.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = ['ugknbfddgicrmopn']
# input = ['aaa']
# input = ['jchzalrnumimnmhp']
# input = ['haegwjzuvuyypxyu']
# input = ['dvszwmarrgswjxmb']
# input = ['qjhvhtzxzqqjkmpb']
# input = ['xxyxx']
# input = ['uurcxstgmygtbstg']
# input = ['ieodomkazucvgmuy']

# Part 1
print 'Part 1'

naughtyCount = 0
niceCount = 0

for str in input:

  naughty = False

  vowelCount = len(re.findall(r'[a,e,i,o,u]', str))
  repeatMatch = re.search(r'([a-z])\1+', str)
  naughtyMatch = re.search(r'(ab)|(cd)|(pq)|(xy)', str)

  if (vowelCount >= 3 and repeatMatch and not naughtyMatch):
    niceCount += 1
  else:
    naughtyCount += 1

print 'Naughty: %i' % naughtyCount
print 'Nice: %i' % niceCount

# Part 2
print '\nPart 2'

naughtyCount = 0
niceCount = 0

for str in input:

  naughty = False

  rule1Match = re.search(r'([a-z]{2}).*\1', str)
  rule2Match = re.search(r'([a-z]).\1', str)

  if (rule1Match and rule2Match):
    niceCount += 1
  else:
    naughtyCount += 1

print 'Naughty: %i' % naughtyCount
print 'Nice: %i' % niceCount