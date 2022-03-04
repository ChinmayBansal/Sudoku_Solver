# Solves maze, contains backtracking algorithm
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, pos):
    #Check if rows are valid.
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[i] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[i]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 +3):
        for j in range(box_x * 3, box_x*3 +3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True
