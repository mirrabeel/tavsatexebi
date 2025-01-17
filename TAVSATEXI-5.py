def safety_check(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if safety_check(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


def num_of_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("შეუძლებელია განლაგება")
        return

    for row in board:
        print(" ".join("Q" if cell == 1 else "_" for cell in row))

n = int(input("შეიყვანეთ n: "))
num_of_queens(n)