import random
list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
goal=random.choice(list1)
number=input("Guess the lowercase alphabet:")
a=0
list2=[]
while number!=goal:
	if number.upper()==number:
		print("please enter a lowercase alphabet:")
		number=input("Guess the lowercase alphabet:")
	else:
		if number< goal:
			print("the alpabet you are looking for is alphabetically higher.")
			a=a+1
			list2.append(number)
			number=input("Guess the lowercase alphabet:")
			continue
		if number> goal:
			print("the alpabet you are looking for is alphabetically lower.")
			a=a+1
			list2.append(number)
			number=input("Guess the lowercase alphabet:")
			continue
print("congratulations! you guess the alphabet "+goal+" in "+str(a)+"tries")
print("guess histogram")
frequency = [0] * 7#七個區間頻率初始是0
for i in list2:
    frequency[(list1.index[i]+1)//4]+= 1#猜出的數字依序在第幾個區間
list3=["a-d","e-h","i-l","m-p","q-t","u-x","y-z"]
result=list(zip(list3,frequency))
for i in range(0,7):
	print(result[i][0]+":",end="")
	print("*"*result[i][1])