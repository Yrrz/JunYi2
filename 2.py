a = int(input())
b = list(range(1,a+1))
c = []
for x in b:
	if x%15==0 :
		c.append(x)
	if ((x%3!=0) and (x%5!=0)):
		c.append(x)
print (len(c))