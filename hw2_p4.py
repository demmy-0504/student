a=int(input("Enter the number of layers(2 to 5)= "))
b=int(input("Enter the side length of the top-triangle is defined between 2 and 6(included)= "))
c=int(input("Enter the growth of each layer= "))
d=int(input("Enter the trunk width(odd number,3 to 9)= ")) 
e=int(input("Enter the trunk height(4 to 10)= "))
f=b-3
sum=0
#等差級數的公式,首項(a1)是 b,n=a,公差(d)=c #an=a1+(n-1)*d
k=b+(a-1)*c-1 #每層第二行的空格數
g=int((k+1-((d-1)/2))) # trunk 的空格數
print(' '*(k+1)+('#')) #print 空格(" "(k+1)......)第一層第一行的空格數
for j in range(0,a):#for j in range 做幾層 layer
	sum=sum+c #sum=sum+c 每層增加的行數
	stars=1#stars=每一行@數
	for i in range (f-1+sum):
		print(' '*(k-i)+('#')+'@'*(stars)+('#')) 
		stars=stars+2
		if i==f-2+sum:
			print(' '*(k-i-1)+'#'*(stars+2)) 
for r in range(1,e+1):
	print(' '*g+'|'*d)