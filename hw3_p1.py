#H24124018 統計系鄭筠潔
list=[]
number=int(input("input the total number of students:"))
for i in range(1,number+1):
	list=list+[i]
while len(list)>1:
	i=(i+3-1)%len(list)
	del list[i]
print("the last ID is :",list[0])
