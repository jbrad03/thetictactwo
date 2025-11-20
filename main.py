# -----------------------------------------
# Two-Player Tic-Tac-Toe (Command Line)
# -----------------------------------------

def create_board():
    return [" " for _ in range(9)]


def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board, player):
    # Winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False


def check_draw(board):
    return " " not in board


def play_game():
    print("Welcome to Tic-Tac-Toe!")

    while True:  # Loop to allow resetting game
        board = create_board()
        current_player = "X"
        game_active = True

        while game_active:
            display_board(board)
            print(f"Player {current_player}'s turn.")

            try:
                move = int(input("Choose a spot (1–9): ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number from 1–9.")
                continue

            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue

            board[move] = current_player

            # Check for winner
            if check_win(board, current_player):
                display_board(board)
                print(f" Player {current_player} wins!")
                game_active = False
            # Check for draw
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                game_active = False
            else:
                # Switch players
                current_player = "O" if current_player == "X" else "X"

        # Ask to play again
        replay = input("Play again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing!")
            break


# Run the game
if __name__ == "__main__":
    play_game()