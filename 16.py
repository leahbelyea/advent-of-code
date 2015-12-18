
with open('input/16.txt', 'r') as f:
  sues = [x.strip('\n') for x in f.readlines()]

with open('input/16-2.txt', 'r') as f:
  analysisInput = [x.strip('\n') for x in f.readlines()]

# Part 1
print 'Part 1'

analysis = {}
for item in analysisInput:
  item = item.split(': ')
  analysis[item[0]] = item[1]

for sue in sues:
  sue = sue.split(' ')
  sueNum = sue[1].replace(':', '')
  sueInfo = {}
  for i in range(2, len(sue) - 1, 2):
    sueInfo[sue[i].replace(':', '')] = sue[i + 1].replace(',', '')
  rejectSue = False
  for compound, level in analysis.iteritems():
    if compound in sueInfo and sueInfo[compound] != level:
      rejectSue = True
      continue
  if rejectSue: continue
  print sueNum
  break

# Part 2
print '\nPart 2'

analysis = {}
for item in analysisInput:
  item = item.split(': ')
  analysis[item[0]] = item[1]

for sue in sues:
  sue = sue.split(' ')
  sueNum = sue[1].replace(':', '')
  sueInfo = {}
  for i in range(2, len(sue) - 1, 2):
    sueInfo[sue[i].replace(':', '')] = sue[i + 1].replace(',', '')
  rejectSue = False
  for compound, level in analysis.iteritems():
    if compound in sueInfo:
      if (compound in ('cats', 'trees') and sueInfo[compound] <= level) or (compound in ('pomeranians', 'goldfish') and sueInfo[compound] >= level) or (compound not in ('cats', 'trees', 'pomeranians', 'goldfish') and sueInfo[compound] != level):
        rejectSue = True
        continue
  if rejectSue: continue
  print sueNum
  break