import random

# 生成迷宮
def generate_maze(N, M):
    # 初始化迷宮字典，所有格子初始為空格（0）
    maze = {(i, j): 0 for i in range(N) for j in range(M)}
    
    # 從左上角到右下角生成一條隨機路徑
    path = [(0, 0)]
    x, y = 0, 0
    while (x, y) != (N-1, M-1):
        if x < N-1 and y < M-1:
            if random.choice([True, False]):
                x += 1
            else:
                y += 1
        elif x < N-1:
            x += 1
        elif y < M-1:
            y += 1
        path.append((x, y))
    
    # 標記路徑格子為2
    for cell in path:
        maze[cell] = 2
    
    return maze

# 添加隨機障礙物
def add_obstacles(maze, min_obstacles, N, M):
    # 確保min_obstacles在有效範圍內
    max_obstacles = N * M - len([cell for cell in maze.values() if cell == 2])
    min_obstacles = min(min_obstacles, max_obstacles)
    
    count = 0
    while count < min_obstacles:
        x, y = random.randint(0, N-1), random.randint(0, M-1)
        if maze[(x, y)] == 0:
            maze[(x, y)] = 1
            count += 1

# 設置障礙物
def set_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinate to set an obstacle, e.g., i,j: ").split(','))
        if x < 0 or x >= N or y < 0 or y >= M:
            print("Error: Coordinates are out of bounds.")
        elif maze[(x, y)] == 2:
            print("Error: Cannot set obstacle on the path.")
        elif maze[(x, y)] == 1:
            print("Error: There is already an obstacle at this location.")
        else:
            maze[(x, y)] = 1
            print(f"Obstacle placed at ({x}, {y})")
    except ValueError:
        print("ValueError in set_obstacle function. Need to be coordinates")

# 移除障礙物
def remove_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinate to remove an obstacle, e.g., i,j: ").split(','))
        if x < 0 or x >= N or y < 0 or y >= M:
            print("Error: Coordinates are out of bounds.")
        elif maze[(x, y)] == 0:
            print("Obstacle does not exist at this location.")
        elif maze[(x, y)] == 2:
            print("Obstacle does not exist on the path.")
        else:
            maze[(x, y)] = 0
            print(f"Obstacle removed at ({x}, {y})")
    except ValueError:
        print("ValueError in remove_obstacle function. Need to be coordinates")
    except KeyError:
        print("KeyError in remove_obstacle function. 'Invalid coordinates. Please input coordinates within the range.'")

# 打印迷宮
def print_maze(maze, N, M):
    print('+' + '---+' * M)
    for i in range(N):
        row = '|'
        for j in range(M):
            if maze[(i, j)] == 0:
                row += '   |'
            elif maze[(i, j)] == 1:
                row += ' X |'
            elif maze[(i, j)] == 2:
                row += ' O |'
        print(row)
        print('+' + '---+' * M)

# 主程序
def main():
    while True:
        filename = input("Enter the maze blueprint filename (grid77.txt or grid99.txt): ")
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            N, M = len(lines), len(lines[0].strip())
            maze = generate_maze(N, M)
            print("Maze generated.")
            break
        except FileNotFoundError:
            print("Error: File not found. Please enter a valid filename.")
        except IOError as e:
            print(f"Error: An I/O error occurred. {e}")

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0:
                raise ValueError
            add_obstacles(maze, min_obstacles, N, M)
            print("Obstacles added.")
            break
        except ValueError:
            print("Error: Invalid number of obstacles. Please enter a valid integer.")

    while True:
        print_maze(maze, N, M)
        print("Options:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Exit")
        option = input("Enter your option: ")
        if option == '1':
            set_obstacle(maze, N, M)
        elif option == '2':
            remove_obstacle(maze, N, M)
        elif option == '3':
            print("Exiting the program.")
            break
        else:
            print("Error: Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()