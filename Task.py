import streamlit as st

st.title(" Sudoku Solver")

# Create a 9x9 grid input
grid = []

st.write("Enter the Sudoku puzzle (use 0 for empty cells):")

for i in range(9):
    cols = st.columns(9)
    row = []
    for j in range(9):
        value = cols[j].number_input(
            f"{i}-{j}",
            min_value=0,
            max_value=9,
            value=0,
            key=f"{i}{j}",
            label_visibility="collapsed"
        )
        row.append(value)
    grid.append(row)

# Function to check if a number is valid
def is_valid(board, row, col, num):
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Backtracking solver
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):
                    if is_valid(board, row, col, num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True

# Solve button
if st.button("Solve Sudoku"):

    board = [row[:] for row in grid]

    if solve(board):

        st.success("Sudoku Solved Successfully!")

        st.write("### Solved Puzzle")

        for row in board:
            st.write(row)

    else:
        st.error("No solution exists for this Sudoku puzzle.")
