import os
import random
import time
import shutil
import keyboard

# 定義顏色常量
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# 定義方向常量
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class SnakeGame:
    def __init__(self):
        self.screen = [[' ' for _ in range(self.get_terminal_width())] for _ in range(self.get_terminal_height())]
        self.obstacles = self.generate_obstacles()  # 產生障礙物
        while True:
            # 重新生成蛇的初始位置，直到不與障礙物或自身碰撞
            self.snake = [(self.get_terminal_height() // 2, self.get_terminal_width() // 2 + i) for i in range(3)]
            if not any(pos in self.snake for pos in self.obstacles):
                break
        self.direction = RIGHT
        self.normal_food_pos = self.place_food('π', [self.snake])
        self.special_food_pos = self.place_food('X', [self.snake, [self.normal_food_pos]])

    # 獲取終端寬度
    def get_terminal_width(self):
        return shutil.get_terminal_size().columns

    # 獲取終端高度
    def get_terminal_height(self):
        return shutil.get_terminal_size().lines

    # 產生隨機位置的食物
    def place_food(self, symbol, avoid_positions):
        while True:
            pos = (random.randint(1, self.get_terminal_height() - 2), random.randint(1, self.get_terminal_width() - 2))
            if pos not in avoid_positions:
                return pos

    # 產生障礙物
    def generate_obstacles(self):
        obstacles = set()
        num_obstacles = (self.get_terminal_height() * self.get_terminal_width()) // 20  # 5% of the screen

        while len(obstacles) < num_obstacles:
            length = random.randint(5, 10)
            if random.choice([True, False]):
                # 水平障礙物
                y, x = random.randint(1, self.get_terminal_height() - 2), random.randint(1, self.get_terminal_width() - length - 1)
                for i in range(length):
                    obstacles.add((y, x + i))
            else:
                # 垂直障礙物
                y, x = random.randint(1, self.get_terminal_height() - length - 1), random.randint(1, self.get_terminal_width() - 2)
                for i in range(length):
                    obstacles.add((y + i, x))

            # 如果障礙物數量超過 5%，則清空障礙物集合重新生成
            if len(obstacles) > num_obstacles:
                obstacles.clear()

        return obstacles

    # 渲染遊戲畫面
    def render_screen(self):
        for i in range(self.get_terminal_height()):
            for j in range(self.get_terminal_width()):
                if (i, j) in self.snake:
                    print(Colors.GREEN + '█' + Colors.RESET, end='')
                elif (i, j) == self.normal_food_pos:
                    print(Colors.YELLOW + 'π' + Colors.RESET, end='')
                elif (i, j) == self.special_food_pos:
                    print(Colors.CYAN + 'X' + Colors.RESET, end='')
                elif (i, j) in self.obstacles:
                    print(Colors.RED + '#' + Colors.RESET, end='')
                else:
                    print(self.screen[i][j], end='')
            print()

    # 遊戲結束
    def game_over(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Game Over!")
        print(f"Normal food eaten: {self.snake.count(self.normal_food_pos)}")
        print(f"Special food eaten: {self.snake.count(self.special_food_pos)}")
        print("Press any key to exit.")

    # 遊戲主循環
    def play_game(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.render_screen()
            time.sleep(0.1)

            # 監聽方向鍵輸入
            if keyboard.is_pressed('w'):
                self.direction = UP
            elif keyboard.is_pressed('s'):
                self.direction = DOWN
            elif keyboard.is_pressed('a'):
                self.direction = LEFT
            elif keyboard.is_pressed('d'):
                self.direction = RIGHT

            # 移動蛇
            if not self.move_snake():
                break

        self.game_over()

    # 移動蛇
    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        # 檢查是否撞到自己或障礙物
        if new_head in self.snake or new_head in self.obstacles:
            return False  # 遊戲結束

        self.snake.insert(0, new_head)

        # 檢查是否吃到食物
        if new_head == self.normal_food_pos:
            self.normal_food_pos = self.place_food('π', [self.snake])
        elif new_head == self.special_food_pos:
            if len(self.snake) > 1:
                self.snake.pop()
            self.special_food_pos = self.place_food('X', [self.snake, [self.normal_food_pos]])
        else:
            self.snake.pop()

        return True


# 遊戲開始
if __name__ == "__main__":
    game = SnakeGame()
    game.play_game()