# main.py

import game_fc

def print_board(board):
    """Print the game board in a readable format."""
    for row in board:
        print('\t'.join(map(str, row)))
    print()

def get_user_move():
    """Get and validate user input for the move."""
    valid_moves = ['w', 'a', 's', 'd']
    while True:
        try:
            move = input("Enter your move (w, a, s, d): ").strip().lower()
            if move in valid_moves:
                return move
            else:
                print("Invalid move. Please enter 'w', 'a', 's', or 'd'.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def main():
    print("Welcome to 2048!")
    print("Use 'w' (up), 'a' (left), 's' (down), 'd' (right) to move the tiles.")
    print("When two tiles with the same number touch, they merge into one!")

    board = game_fc.initialize_game()
    print_board(board)

    while True:
        move = get_user_move()

        if move == 'w':
            board = game_fc.move_up(board)
        elif move == 's':
            board = game_fc.move_down(board)
        elif move == 'a':
            board = game_fc.move_left(board)
        elif move == 'd':
            board = game_fc.move_right(board)

        game_fc.add_new_2(board)
        print_board(board)

        state = game_fc.get_current_state(board)
        if state == 'WON':
            print("Congratulations! You've won the game!")
            break
        elif state == 'LOST':
            print("Game Over! Try again.")
            break

    if input("Do you want to play again? (yes/no): ").strip().lower() == 'yes':
        main()

if __name__ == "__main__":
    main()
