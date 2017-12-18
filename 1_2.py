a = input()
li = a.split( )
putstr = []
print (li)
for x in li:
	putstr.append(''.join(reversed(x)))
out = ' '.join(putstr)
print (out)