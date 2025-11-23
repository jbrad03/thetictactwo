# -----------------------------------------
# Two-Player Tic-Tac-Toe with AI (Command Line)
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


def display_board_with_positions():
    """Show players which number corresponds to which board position."""
    print("Position guide:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def check_win(board, player):
    """Check if the given player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)


def check_draw(board):
    """Check if the board is full (draw condition)."""
    return " " not in board


def get_available_moves(board):
    """Return a list of available positions on the board."""
    return [i for i in range(9) if board[i] == " "]


def get_player_move(board):
    """Get and validate player input for their move."""
    while True:
        try:
            move = int(input("Choose a spot (1–9): ")) - 1
            
            if move < 0 or move > 8:
                print("❌ Please enter a number between 1 and 9.")
                continue
            
            if board[move] != " ":
                print("❌ That spot is already taken. Try again.")
                continue
            
            return move
        except ValueError:
            print("❌ Invalid input. Please enter a number from 1 to 9.")


def minimax(board, depth, is_maximizing, ai_player, human_player):
    """
    Minimax algorithm to evaluate the best move for the AI.
    Returns a score: 10 for AI win, -10 for human win, 0 for draw.
    """
    if check_win(board, ai_player):
        return 10 - depth
    if check_win(board, human_player):
        return depth - 10
    if check_draw(board):
        return 0
    
    if is_maximizing:  # AI's turn (maximize score)
        max_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = ai_player
            score = minimax(board, depth + 1, False, ai_player, human_player)
            board[move] = " "
            max_score = max(score, max_score)
        return max_score
    else:  # Human's turn (minimize score)
        min_score = float('inf')
        for move in get_available_moves(board):
            board[move] = human_player
            score = minimax(board, depth + 1, True, ai_player, human_player)
            board[move] = " "
            min_score = min(score, min_score)
        return min_score


def get_ai_move(board, ai_player):
    """
    Determine the best move for the AI using minimax algorithm.
    """
    human_player = "O" if ai_player == "X" else "X"
    best_score = -float('inf')
    best_move = None
    
    for move in get_available_moves(board):
        board[move] = ai_player
        score = minimax(board, 0, False, ai_player, human_player)
        board[move] = " "
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move


def get_gamemode():
    """Allow player to choose between PVP and PVE (AI) modes."""
    while True:
        print("=" * 35)
        print("  Select Game Mode")
        print("=" * 35)
        print("1. PVP (Player vs Player)")
        print("2. PVE (Player vs AI)")
        print()
        
        choice = input("Choose a mode (1 or 2): ").strip()
        
        if choice == "1":
            return "pvp"
        elif choice == "2":
            return "pve"
        else:
            print("❌ Invalid choice. Please enter 1 or 2.\n")


def play_pvp():
    """Player vs Player game mode."""
    board = create_board()
    current_player = "X"
    game_active = True

    while game_active:
        display_board(board)
        print(f"Player {current_player}'s turn")
        print("-" * 35)
        
        move = get_player_move(board)
        board[move] = current_player

        if check_win(board, current_player):
            display_board(board)
            print("=" * 35)
            print(f"🎉 Player {current_player} wins!")
            print("=" * 35)
            game_active = False
        elif check_draw(board):
            display_board(board)
            print("=" * 35)
            print("🤝 It's a draw!")
            print("=" * 35)
            game_active = False
        else:
            current_player = "O" if current_player == "X" else "X"


def play_pve():
    """Player vs AI game mode."""
    board = create_board()
    human_player = "X"
    ai_player = "O"
    game_active = True

    print("\nYou are X, AI is O")
    print("-" * 35)

    while game_active:
        # Human's turn
        display_board(board)
        print(f"Your turn (Player {human_player})")
        print("-" * 35)
        
        move = get_player_move(board)
        board[move] = human_player

        if check_win(board, human_player):
            display_board(board)
            print("=" * 35)
            print("🎉 You win!")
            print("=" * 35)
            game_active = False
        elif check_draw(board):
            display_board(board)
            print("=" * 35)
            print("🤝 It's a draw!")
            print("=" * 35)
            game_active = False
        else:
            # AI's turn
            print("\n🤖 AI is thinking...")
            move = get_ai_move(board, ai_player)
            board[move] = ai_player

            if check_win(board, ai_player):
                display_board(board)
                print("=" * 35)
                print("🤖 AI wins! Better luck next time!")
                print("=" * 35)
                game_active = False
            elif check_draw(board):
                display_board(board)
                print("=" * 35)
                print("🤝 It's a draw!")
                print("=" * 35)
                game_active = False


def play_game():
    """Main game loop with gamemode selection."""
    print("=" * 35)
    print("  Welcome to Tic-Tac-Toe!")
    print("=" * 35)
    display_board_with_positions()

    while True:
        gamemode = get_gamemode()
        print()

        if gamemode == "pvp":
            play_pvp()
        else:  # pve
            play_pve()

        # Ask to play again
        while True:
            replay = input("Play again? (y/n): ").lower().strip()
            if replay in ["y", "n"]:
                break
            print("❌ Please enter 'y' or 'n'.")
        
        if replay != "y":
            print("Thanks for playing! Goodbye! 👋")
            break
        print()


if __name__ == "__main__":
    play_game()