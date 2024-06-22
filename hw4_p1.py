import random
def game format (matrix):
print ("a","b","c","d","e","f","g","h")
for i in range (9) :
	print("1+1+---1*9+1+1")
	print ("i+1, end=' ") 
	for j in range (9) :	
	print (' |', matrix[i] [j],'',end="")
	if j==8:
	print (' |')
#設置地雷的函数
#def set mine (matrix) :
#return matrix
＃設置旗子
def set flag(row, col, matrix)
matrix[row-11][col-11]=IFI
#計算相鄰有幾顆炸彈
def count mines (row, col, matrix) :
count = 0
for i in range (row-1, row+2) :
for j in range (col-1, col+2) :
if i >=0 and i< 9 and j >= 0 and < 9 and matrix[ild] ==xr:
count += 1 if count > 0:
matrix [row] [col] = str (count)