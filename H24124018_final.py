def parse_matrix(matrix_str):
    """解析輸入的字串成為字典形式的二維矩陣。"""
    rows = matrix_str.split('|')
    matrix = {}
    for i, row in enumerate(rows):
        elements = row.split(',')
        for j, element in enumerate(elements):
            matrix[(i, j)] = int(element)
    return matrix

def matrix_multiply(U, V, n):
    """相乘兩個字典形式的矩陣 U 和 V。"""
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U.get((i, k), 0) * V.get((k, j), 0) for k in range(n))
    return M

def print_matrix(matrix, n):
    """以指定的格式輸出字典形式的矩陣。"""
    for i in range(n):
        row = [matrix.get((i, j), 0) for j in range(n)]
        print(row)

def main():
    # 讀取矩陣 U 和 V
    U_str = input("Enter matrix U: ")
    V_str = input("Enter matrix V: ")

    # 解析矩陣
    U = parse_matrix(U_str)
    V = parse_matrix(V_str)
    
    # 假設矩陣是 n x n 的，從 U_str 的行數可以得知 n
    n = len(U_str.split('|'))

    # 相乘矩陣
    M = matrix_multiply(U, V, n)

    # 輸出結果
    print("M = U x V")
    print_matrix(M, n)

# 執行主程式
if __name__ == "__main__":
    main()