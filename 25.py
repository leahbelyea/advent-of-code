codeRow = 2978
codeColumn = 3083
code = 20151125

# Part 1
print 'Part 1'

n = (codeRow - 1) + (codeColumn - 1)
position = (n * (n + 1) / 2) + (codeColumn - 1) + 1

for i in range(position - 1):
  code = (code * 252533) % 33554393

print code


