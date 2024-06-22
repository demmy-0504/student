p=input("input polynomial:")
v=input("input the value:")
p2=p.replace("x",v)
p3=p2.replace("^"," ^ ")
p4=p3.replace("*"," * ")
p5=p4.replace("+"," + ")
p6=p5.replace("-"," - ")
list1=p6.split(' ')
for i in range(0,len(list1)-1):
	if list1[i]=="^":
		val=int(list1[i-1])**int(list1[i+1])
		del list1[i-1:i+2]
		list1.insert(i-1,val)#為何這行是正確的
	elif i==len(list1)-1:
		break
for i in range(0,len(list1)-1):
	if list1[i]=="*":
		val2=int(list1[i-1])*int(list1[i+1])
		del list1[i-1:i+2]
		list1.insert(i-1,val2)#為何這行是正確的
	elif i==len(list1)-1:
		break
list2=[]
list3=[]
if list1[0]!=("+"and"-"and" "):
	list3=list3+[int(list1[0])]
for i in  range(0,len(list1)-1):
	if list1[i]=="-":
		list2=list2+[int(list1[i+1])]
	elif list1[i]=="+":
		list3=list3+[int(list1[i+1])]
result=sum(list3)-sum(list2)
print("evaluted result:",result)




