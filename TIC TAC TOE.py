import math


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_winner(board, player):
    # Check rows, columns, and diagonals
    return any(
        all(board[i][j] == player for j in range(3)) or  # Rows
        all(board[j][i] == player for j in range(3)) or  # Columns
        all(board[j][j] == player for j in range(3)) or  # Main diagonal
        all(board[j][2 - j] == player for j in range(3))  # Anti-diagonal
        for i in range(3)
    )


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']


def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    return move


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'")
    print_board(board)

    while True:
        # Player Move
        row, col = map(int, input("Enter your move (row and column: 0-2): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'

        if is_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI Move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'

        print("AI plays:")
        print_board(board)

        if is_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
