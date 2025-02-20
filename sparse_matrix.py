class SparseMatrix:
    def __init__(self, file_path):
        """Initialize the sparse matrix from a file."""
        self.num_rows = 0
        self.num_cols = 0
        self.values = {}

        self.load_from_file(file_path)

    def load_from_file(self, file_path):
        """Read the matrix from a file and store it as a dictionary."""
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()

                for line in lines:
                    line = line.strip()
                    if not line:
                        continue

                    if line.startswith("rows="):
                        self.num_rows = int(line.split("=")[1])
                    elif line.startswith("cols="):
                        self.num_cols = int(line.split("=")[1])
                    elif line.startswith("(") and line.endswith(")"):
                        parts = line[1:-1].split(",")
                        row, col, val = map(int, parts)
                        self.values[(row, col)] = val
                    else:
                        raise ValueError("Invalid input format")

        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
        except ValueError as e:
            print(f"Error: {e}")

    def display(self):
        """Print the matrix in a readable format."""
        print(f"Sparse Matrix ({self.num_rows}x{self.num_cols}):")
        for (row, col), value in self.values.items():
            print(f"Row {row}, Col {col} → {value}")

    def __add__(self, other):
        """Add two sparse matrices."""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix sizes do not match for addition")

        result = SparseMatrix.__empty_matrix(self.num_rows, self.num_cols)

        for key in set(self.values.keys()).union(other.values.keys()):
            result.values[key] = self.values.get(key, 0) + other.values.get(key, 0)

        return result

    def __sub__(self, other):
        """Subtract two sparse matrices."""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix sizes do not match for subtraction")

        result = SparseMatrix.__empty_matrix(self.num_rows, self.num_cols)

        for key in set(self.values.keys()).union(other.values.keys()):
            result.values[key] = self.values.get(key, 0) - other.values.get(key, 0)

        return result

    def __mul__(self, other):
        """Multiply two sparse matrices."""
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix sizes do not match for multiplication")

        result = SparseMatrix.__empty_matrix(self.num_rows, other.num_cols)

        for (row, col), value in self.values.items():
            for k in range(other.num_cols):
                if (col, k) in other.values:
                    result.values[(row, k)] = result.values.get((row, k), 0) + value * other.values[(col, k)]

        return result

    def save_to_file(self, file_path):
        """Save the sparse matrix to a file."""
        with open(file_path, "w") as file:
            file.write(f"rows={self.num_rows}\n")
            file.write(f"cols={self.num_cols}\n")

            for (row, col), value in sorted(self.values.items()):
                file.write(f"({row}, {col}, {value})\n")

    @staticmethod
    def __empty_matrix(rows, cols):
        """Create an empty sparse matrix (helper method)."""
        matrix = SparseMatrix.__new__(SparseMatrix)
        matrix.num_rows = rows
        matrix.num_cols = cols
        matrix.values = {}
        return matrix
