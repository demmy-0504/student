a=input("enter a sequence of integers separated by whitespace:")
b=a.split(" ")#把輸入的數字變成列表形式
intlist=[int(i) for i in b]#把列表裡的字串形式改成數字
list2=[]+[min(intlist)]#找到最小的數字
for j in range(0,len(intlist)-1):
	if intlist[j]==min(intlist):
		d=j#找到最小的數字他在第幾個
for i in range(d,len(intlist)-1):
	if intlist[i+1]>intlist[i]:
		list2=list2+[intlist[i+1]]#連續則放入結果列表
	else:
		break#不連續則跳出迴圈
print("length:",len(list2))
print("LICS:",list2)