# Sudoku Solver

A simple and interactive **Sudoku Solver Web App** built using **Python** and **Streamlit**.  
Users can enter a Sudoku puzzle, and the application solves it using a **Backtracking Algorithm**.

##  Features

- Interactive 9×9 Sudoku grid input
- Uses `0` to represent empty cells
- Automatically validates Sudoku rules
- Solves puzzles using recursion and backtracking
- Displays the solved Sudoku grid
- Shows an error message if no solution exists

##  Technologies Used

- Python
- Streamlit

##  Project Structure

```
Sudoku-Solver/
│
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Required dependencies
```

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Sudoku-Solver.git
```

### 2. Navigate into the project folder

```bash
cd Sudoku-Solver
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

##  Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser.

##  How to Use

1. Enter Sudoku values in the 9×9 grid.
2. Keep empty cells as `0`.
3. Click the **Solve Sudoku** button.
4. The solved puzzle will be displayed.

##  Algorithm Used

This project uses the **Backtracking Algorithm**.

### Working Process:

1. Find an empty cell.
2. Try numbers from `1` to `9`.
3. Check if the number is valid:
   - Not repeated in the row
   - Not repeated in the column
   - Not repeated in the 3×3 sub-grid
4. Place the number if valid.
5. Recursively solve the remaining puzzle.
6. Backtrack if a conflict occurs.

##  Example Input

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

##  Example Output

```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

##  Requirements

Create a `requirements.txt` file:

```
streamlit
```

##  License

This project is open-source and available under the MIT License.
