def is_valid(board, row, col, n):
    # Y
    for i in range(n):
        if board[i][col] == 'X':
            return False
    # Y right
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 'X':
            return False
        i, j = i-1, j+1
    # Y left
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'X':
            return False
        i, j = i-1, j-1
    # OK
    return True


def place_queens(board, row, n):
    if row == n:
        return True
    else:
        for col in range(n):
            if is_valid(board, row, col, n):
                board[row][col] = 'X'
                if place_queens(board, row+1, n):
                    return True
                board[row][col] = 'O'
        return False


n = int(input("Entrez la taille du plateau de jeu : "))
board = [['O' for i in range(n)] for j in range(n)]
if place_queens(board, 0, n):
    for row in board:
        print(' '.join(row))
else:
    print("Aucune solution n'a été trouvée.")
