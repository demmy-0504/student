money=int(input("Enter the shopping amount:"))
# 讓使用者輸入數值並把他轉成數字型
level=input("Enter the membership level (regular or gold):")
#讓使用者輸入regular or gold
if 6<len(level)<8 :
	if 0<=money<=1000:
		total=money
	if 1000<money<=2000:
		total=money*0.9
	if 2000<money<=3000:
		total=money*0.85
	if 3000<money:
		total=money*0.8
		#要讓系統判斷是regular所以用len計算要等於7
		#另一個新的變數在規定的範圍內成以適當的打折
elif 3<len(level)<5:
	if 0<=money<=1000:
		total=money
	if 1000<money<=2000:
		total=money*0.85
	if 2000<money<=3000:
		total=money*0.8
	if 3000<money:
		total=money*0.75
		#要讓系統判斷是regular所以用len計算要等於4
		#另一個新的變數在規定的範圍內成以適當的打折
else:
	print("invalid membership level")
	#不適regular and gold 會print出的內容
print(level+$+str(total))
#最後會print出的內容加起來

