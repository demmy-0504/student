size=int(input("enter the size of the grid"))
rows,cols=size,size
matrix=[["- "]*cols for _ in range(rows)]#列出矩陣
for row in matrix:
	print(" ".join(row))#print出矩陣
c=input("enter the cell coordinates to edit:")
while c!="done":#題目條件:直到輸入為done時停止
	v=input("enter the new value for the cell:")
	row, col = map(int, c.split(','))#把列表裡的數字字串形式改為數字形式
	matrix[row][col]=v#把輸入的座標改為指定文字
	for row in matrix:
		print(" ".join(row))#print出矩陣
	c=input("enter the cell coordinates to edit:")
	if c=="done":
		break
	v=input("enter the new value for the cell:")