import random

def generate_board(level):
    """Generate a 4x4 to 15x15 Sudoku board based on the level."""
    size = 4 + level // 50
    board = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = random.randint(1, size)
    return board

def print_board(board):
    """Print the board in a human-readable format."""
    size = len(board)
    for i in range(size):
        if i % (size // 3) == 0 and i != 0:
            print("- " * (size + (size // 3) - 1))
        for j in range(size):
            if j % (size // 3) == 0 and j != 0:
                print("| ", end="")
            if j == size - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def is_valid(board, num, pos):
    """Check if a number can be placed in a given position."""
    size = len(board)
    # Check row
    for i in range(size):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(size):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check square
    square_x = pos[1] // (size // 3)
    square_y = pos[0] // (size // 3)
    for i in range(square_y * (size // 3), square_y * (size // 3) + (size // 3)):
        for j in range(square_x * (size // 3), square_x * (size // 3) + (size // 3)):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    """Solve the Sudoku puzzle."""
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                for num in range(1, size + 1):
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def main():
    """Main function for the game."""
    level = int(input("Enter level (1-500): "))
    sublevel = int(input("Enter sublevel (1-200): "))
    board = generate_board(level)
    print_board(board)
    print("\nSolving puzzle...")
    solve(board)
    print_board(board)

if __name__ == "__main__":
    main()
