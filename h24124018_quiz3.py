print("welcome to the simple calculator program!")
result=0 #設定一開始的變數為0
willing=True #讓willing=true 以至於下面的while迴圈可繼續進行
while True:
	a=float(input("enter the first number:"))#讓使用者輸入數字並把他轉成浮點數
	b=float(input("enter the second number:"))#讓使用者輸入數字並把他轉成浮點數
	s=input("select an arithmetic operation(+,-,*,/):")#讓使用者輸入選擇
	if s=="+":#條件判斷s=哪一個運算選擇然後再繼續下去
		result=a+b
		print("result:",str(result))#並列印出來
	elif s=="-":
		result=a-b
		print("result:",str(result))
	elif s=="/":
		if b==0:#如果分母為0讓他直接回到迴圈一開始-使用者輸入數字
			print("division by zero")
			continue
		else:
			result=a/b
			print("result:",result)
	elif s=="*":
		result=a*b
		print("result:",str(result))
	c=input("do you want to perform another calculation?(yes or no)")#詢問使用者是否繼續
	if c=="yes":
		continue #continue 表回到迴圈一開始
	elif c=="no":
		willing==False #讓willing=false 所以迴圈無法繼續而停止
		print("good bye!")#程式結束










