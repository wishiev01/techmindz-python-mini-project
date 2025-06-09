#tic tac toe game

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  
            return True
        if all([board[j][i] == player for j in range(3)]):  
            return True
        
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def play_game():
    board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        move = input(f"Player {current_player}, choose a position (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Choose a number between 1 and 9.")
            continue

        row = (int(move)-1) // 3
        col = (int(move)-1) % 3

        if board[row][col] in ['X', 'O']:
            print("That spot is already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
