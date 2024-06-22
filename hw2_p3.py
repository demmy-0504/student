y=int(input("please innput the year:"))
m=int(input("please input the month"))
if m==2:
	if (y%4==0 and y%100!=0)or y%400==0: #可被4整除但不被100整除或是被400整除的年份是閏年
		days=29
	else:
		days=28
elif m in[4,6,9,11]:
	days=30
else:
	days=31
y=y-1
k=y%100
j=y//100
w=(1+13*(m+1)//5+k+j//4+5*j)%7 #這條公式網路上查不到 #到這算出某年某月的第一天在星期幾了
print("Sun Mon Tue Wed Thu Fri Sat")
# print(" "*((w%7+7)%7),end="") #這公式怎麼出來的
# for i in range(1,days+1):#看不懂
# 	print("{0:3d}".format(i),end="")#看不懂
# 	if (i+(w%7+7)%7)%7==0:#看不懂
# 		print()#打出的程式是錯誤的
print(""*2*w,end="")
for i in range(1,days+1):
	if i<=10:
		print("0"+str(i)+"",end="")
	else:
		print(str(i)+"",end="")
	if (w+i)%7==0:
		print(""+"\n")