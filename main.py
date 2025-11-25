import random

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
    print("Position guide:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)


def check_draw(board):
    return " " not in board


def get_available_moves(board):
    return [i for i in range(9) if board[i] == " "]


def get_player_move(board):
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


# ----------------------------
# MINIMAX (Hard)
# ----------------------------

def minimax(board, depth, is_maximizing, ai_player, human_player):
    if check_win(board, ai_player):
        return 10 - depth
    if check_win(board, human_player):
        return depth - 10
    if check_draw(board):
        return 0
    
    if is_maximizing:
        max_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = ai_player
            score = minimax(board, depth + 1, False, ai_player, human_player)
            board[move] = " "
            max_score = max(score, max_score)
        return max_score
    else:
        min_score = float('inf')
        for move in get_available_moves(board):
            board[move] = human_player
            score = minimax(board, depth + 1, True, ai_player, human_player)
            board[move] = " "
            min_score = min(score, min_score)
        return min_score


# -------------------------------------------------------------
# AI MOVE with Difficulty Setting
# -------------------------------------------------------------

def get_ai_move(board, ai_player, difficulty):
    human_player = "O" if ai_player == "X" else "X"

    # EASY = random move
    if difficulty == "easy":
        return random.choice(get_available_moves(board))

    # MEDIUM = 50% chance minimax, 50% random
    if difficulty == "medium":
        if random.random() < 0.5:
            return random.choice(get_available_moves(board))
        # else fall through to minimax

    # HARD = always minimax
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


# ----------------------------
# GET DIFFICULTY
# ----------------------------

def get_difficulty():
    while True:
        print("=" * 35)
        print("     Select AI Difficulty")
        print("=" * 35)
        print("1. Easy (Random Moves)")
        print("2. Medium (Mixed Random + Smart)")
        print("3. Hard (Unbeatable Minimax)")
        print()

        choice = input("Choose difficulty (1-3): ").strip()

        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("❌ Invalid choice. Enter 1–3.\n")


def get_player_marker():
    while True:
        print("=" * 35)
        print("    Choose Your Marker")
        print("=" * 35)
        print("X = Crosses (goes first)")
        print("O = Circles (goes second)")
        print()

        choice = input("Do you want to be X or O? ").strip().upper()

        if choice in ("X", "O"):
            return choice
        else:
            print("❌ Invalid choice. Enter X or O.\n")


# ----------------------------
# GAME MODES
# ----------------------------

def play_pvp():
    board = create_board()
    current_player = "X"

    while True:
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
            return
        elif check_draw(board):
            display_board(board)
            print("=" * 35)
            print("🤝 It's a draw!")
            print("=" * 35)
            return
        
        current_player = "O" if current_player == "X" else "X"


def play_pve():
    board = create_board()
    # Let the player choose their marker. Crosses (X) always go first.
    player_choice = get_player_marker()
    human_player = player_choice
    ai_player = "O" if human_player == "X" else "X"

    if human_player == "X":
        print("\nYou are X (Crosses) — you go first.")
    else:
        print("\nYou are O (Circles) — AI goes first.")

    print(f"You are {human_player}, AI is {ai_player}")
    print("-" * 35)

    difficulty = get_difficulty()

    # Crosses (X) always start first
    current_turn = "X"

    while True:
        # Human's turn when the current turn matches their marker
        if current_turn == human_player:
            display_board(board)
            print("Your turn!")
            print("-" * 35)

            move = get_player_move(board)
            board[move] = human_player

            if check_win(board, human_player):
                display_board(board)
                print("=" * 35)
                print("🎉 You win!")
                print("=" * 35)
                return
            elif check_draw(board):
                display_board(board)
                print("=" * 35)
                print("🤝 It's a draw!")
                print("=" * 35)
                return
        else:
            # AI's turn
            display_board(board)
            print("\n🤖 AI is thinking...")
            ai_move = get_ai_move(board, ai_player, difficulty)
            board[ai_move] = ai_player

            if check_win(board, ai_player):
                display_board(board)
                print("=" * 35)
                print("🤖 AI wins!")
                print("=" * 35)
                return
            elif check_draw(board):
                display_board(board)
                print("=" * 35)
                print("🤝 It's a draw!")
                print("=" * 35)
                return

        # Switch turns
        current_turn = "O" if current_turn == "X" else "X"


# ----------------------------
# MAIN MENU
# ----------------------------

def get_gamemode():
    while True:
        print("=" * 35)
        print("        Select Game Mode")
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


def play_game():
    print("=" * 35)
    print("      Welcome to Tic-Tac-Toe!")
    print("=" * 35)
    display_board_with_positions()

    while True:
        gamemode = get_gamemode()
        print()

        if gamemode == "pvp":
            play_pvp()
        else:
            play_pve()

        replay = input("Play again? (y/n): ").lower().strip()
        if replay != "y":
            print("Thanks for playing! Goodbye! 👋")
            break
        print()


if __name__ == "__main__":
    play_game()
