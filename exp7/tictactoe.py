import math

WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]             
]

def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def evaluate(board):
    """Calculates E = (Lines X can win) - (Lines O can win)."""
    x_lines = 0
    o_lines = 0
    for line in WIN_LINES:
        values = [board[i] for i in line]
        if 'O' not in values: x_lines += 1
        if 'X' not in values: o_lines += 1
    return x_lines - o_lines

def check_winner(board):
    for line in WIN_LINES:
        if board[line[0]] == board[line[1]] == board[line[2]] and board[line[0]] != ' ':
            return board[line[0]] 
    if ' ' not in board:
        return 'Draw'
    return None

def is_terminal(board):
    return check_winner(board) is not None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return 1 
    if winner == 'O': return -1 
    if winner == 'Draw': return 0
    
    if depth == 0:
        return evaluate(board)

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval_score = minimax(board, depth - 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval_score = minimax(board, depth - 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval_score)
        return min_eval

def get_ai_move(board, depth_limit=4):
    """Finds the best move for 'O' (Minimizer)."""
    best_score = math.inf
    best_move = -1
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' # Try move
            # Next turn is X, so is_maximizing is True
            move_score = minimax(board, depth_limit - 1, True)
            board[i] = ' ' # Undo move
            
            # Since AI is 'O', it wants the LOWEST possible score
            if move_score < best_score:
                best_score = move_score
                best_move = i
                
    return best_move

def play_game():
    board = [' '] * 9
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the AI is 'O'.")
    print("Positions are numbered 1-9, mapping left-to-right, top-to-bottom.")
    
    demo_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board(demo_board)
    print("Let's begin!")
    
    while True:
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("Invalid move! Spot is taken or out of bounds. Try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
                
        print_board(board)
        
        if is_terminal(board):
            break

        print("AI is thinking...")
        ai_idx = get_ai_move(board, depth_limit=4)
        board[ai_idx] = 'O'
        print(f"AI plays at position {ai_idx + 1}:")
        print_board(board)
        
        if is_terminal(board):
            break

    result = check_winner(board)
    if result == 'X':
        print("Congratulations! You won!")
    elif result == 'O':
        print("The AI wins! Better luck next time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()