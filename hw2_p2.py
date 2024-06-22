number=int(input("input the range number:"))

for n in range(1,number):
		sum=0
		for i in range(1,n):
				if n % i ==0:
						sum=sum+i
		if sum==n:
				print(n,"\n")