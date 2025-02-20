                   Sparse Matrix Operations

Project Overview
This project implements efficient operations for Sparse Matrices, which contain mostly zero values. Instead of storing the entire matrix in memory, we use a dictionary-based representation to store only nonzero elements. This makes our solution memory-efficient and fast, especially for large matrices.

Features
- Memory-efficient storage using dictionaries.
- Fast matrix operations (Addition, Subtraction, Multiplication).
- Handles large matrices (e.g., 8433 × 3180) without performance issues.
- Saves and loads matrices from files.

Project Structure
.
├── sparse_matrix.py       # Implementation of the SparseMatrix class
├── matrix_operations.py   # Script to perform operations on matrices
├── matrix1.txt            # Example input file (Matrix 1)
├── matrix2.txt            # Example input file (Matrix 2)
├── result_add.txt         # Output file (Addition result)
├── result_sub.txt         # Output file (Subtraction result)
├── result_mul.txt         # Output file (Multiplication result)
├── README.md              # Project documentation (this file)

How It Works
Matrix Representation
- The matrix is stored in a dictionary {(row, col): value}.
- Example:
  python
  { (0, 2): 5, (1, 1): 8, (2, 3): -3 }
  
  This represents a matrix where only these positions have nonzero values.

File Format
Each matrix file follows this format:
rows=4
cols=5
(0,2,5)
(1,1,8)
(2,3,-3)

- rows=x and cols=y define the matrix dimensions.
- Each (row, col, value) represents a nonzero entry.

Operations Supported
- Addition: matrix1 + matrix2
- Subtraction: matrix1 - matrix2
- Multiplication: matrix1 × matrix2

Usage Guide
Install Python (if not installed)
Ensure you have Python 3 installed:
Run
python3 --version


Run the Script
Run
python3 matrix_operations.py

You'll be prompted to choose an operation:

Choose operation: add, subtract, multiply


Check Output Files
Results are saved in:
- Addition: result_add.txt
- Subtraction: result_sub.txt
- Multiplication: result_mul.txt




