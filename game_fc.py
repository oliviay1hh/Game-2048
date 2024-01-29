import random

def initialize_game():
    """Initialize the game board with two '2's in random positions."""
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_2(board)
    add_new_2(board)
    return board

def add_new_2(board):
    """Add a new '2' to a random empty cell on the board."""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2

def compress(board):
    """Compress the non-empty cells to the left."""
    new_board = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][position] = board[i][j]
                position += 1
    return new_board

def merge(board):
    """Merge cells with the same values."""
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse(board):
    """Reverse the rows of the board."""
    new_board = []
    for i in range(4):
        new_board.append(board[i][::-1])
    return new_board

def transpose(board):
    """Transpose the board."""
    new_board = [[board[j][i] for j in range(4)] for i in range(4)]
    return new_board

def move_left(board):
    """Make a left move."""
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    """Make a right move."""
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board):
    """Make an upward move."""
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):
    """Make a downward move."""
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def get_current_state(board):
    """Check the current state of the game."""
    # Check for win
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return 'WON'

    # Check if there are no zero entries
    if any(0 in row for row in board):
        return 'GAME NOT OVER'

    # Check for possible moves after no zero entries
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i + 1][j] or board[i][j] == board[i][j + 1]:
                return 'GAME NOT OVER'

    for j in range(3):
        if board[3][j] == board[3][j + 1]:
            return 'GAME NOT OVER'

    for i in range(3):
        if board[i][3] == board[i + 1][3]:
            return 'GAME NOT OVER'

    return 'LOST'
