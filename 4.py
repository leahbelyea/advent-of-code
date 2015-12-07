import hashlib
import datetime

input = 'yzbqklnj'
# input = 'abcdef'
# input = 'pqrstuv'

# Part 1
print 'Part 1'

num = 1
while (True):
	hash = hashlib.md5(input + str(num)).hexdigest()
	if (hash[:5] == '00000'):
		print num
		break
	num +=1

# Part 2
print '\nPart 2'

# No need to reset num; the first number to produce five leading 0s would also be the first that could potentially produce 6 leading 0s
while (True):
	hash = hashlib.md5(input + str(num)).hexdigest()
	if (hash[:6] == '000000'):
		print num
		break
	num +=1
