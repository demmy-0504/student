seat=input("input sequence of seats:")
a=seat.split(" ")
b=[int(i) for i in a]
c=b[:]
c.reverse()
number=0
sum=0
for r in range(1,max(b)+1):
	for i in range(0,len(b)):
		if b[i]>=r:
			start=i
			break
		else:
			continue
	for k in range(0,len(c)):
		if c[k]>=r:
			end=len(b)-1-k
			break
		else:
			continue
	for j in range(i+1,len(b)-1-k):
		if b[j]>=r:
			number+=1
		else:
			continue
	if len(b)-1-k!=i:
		sum+=len(b)-1-k-i-1-number
	number=0
print("water="+str(sum))
