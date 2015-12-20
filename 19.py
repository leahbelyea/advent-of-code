import re

with open('input/19.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

def replaceNth(haystack, needle, replacement, n):
  occurrences = 0
  haystack = list(haystack.replace(needle, '#'))
  for i in range(len(haystack)):
    if haystack[i] == '#':
      occurrences += 1
      if occurrences == n:
        haystack[i] = replacement
      else:
        haystack[i] = needle
  return ''.join(haystack)

# Part 1
print 'Part 1'

replacements = {}
medicineMolecule = input.pop()

for item in input:
  item = item.split(' => ')
  if len(item) >= 2:
    if item[0] in replacements:
      replacements[item[0]].append(item[1])
    else:
      replacements[item[0]] = [item[1]]

molecules = []
for letters, replacementList in replacements.iteritems():
  matches = re.findall(letters, medicineMolecule)
  for i in range(1, len(matches) + 1):
    for j in range(len(replacementList)):
      molecules.append(replaceNth(medicineMolecule, letters, replacementList[j], i))

print len(set(molecules))

# Part 2
print '\nPart 2'

replacements = {}

for item in input:
  item = item.split(' => ')
  if len(item) >= 2:
    replacements[item[1]] = item[0]

steps = 0

while len(re.findall(r'[^e]', medicineMolecule)) > 0:
  matches = []
  for letters, replacement in replacements.iteritems():
    numMatches = len(re.findall(letters, medicineMolecule))
    if numMatches > 0:
      matches.append((letters, numMatches))
  matches = sorted(matches, key=lambda match: match[1])
  # Assume best match is the less frequent one
  bestMatch = matches[0][0]
  medicineMolecule = medicineMolecule.replace(bestMatch, replacements[bestMatch])
  steps += matches[0][1]

print steps
