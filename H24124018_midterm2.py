import random
#創建一個列表有N個元素裡面各有M個且初始皆設為0
def generate_path(N,M):
	maze=[]
	for i in range(N):
		row=[]
		for j in range(M):
			row.append(0)
		maze.append(row)
	return maze
def add_obstacles(maze,num_obstacles):
	indexs=[i for i in range(N*M)]
	mine_indexs=random.sample(indexs,num_obstacles)#隨機選指定數量的障礙
	for j in mine_indexs:#選出來的元素在第幾列第幾行
		row=j//N
		col=j% M
		maze[row-1][col-1]="X"#選到的替換成X
	return maze
def generate_maze(N,M,num_obstacles):
	maze=generate_path(N,M)
	maze=add_obstacles(maze,num_obstacles)
	return maze
def print_maze(maze):
	print("+"+"---+"*len(maze[0]))#畫出圖形
	for i in range(len(maze)):
		row_str="|"
		for j in range(len(maze[0])):
			if maze[i][j]==0:#如果是一般無障礙的情況
				row_str+="   "
			elif maze[i][j]=="X":#如果是障礙物的形況
				row_str+=" X "	
			row_str+="|"
		print(row_str)
		print("+"+"---+"*len(maze[0]))
N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N*M-(N+M-1)#最大可輸入的障礙物值
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))#如果超出
print(print_maze(generate_maze(N,M,num_obstacles)))