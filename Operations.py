from sparse_matrix import SparseMatrix

if __name__ == "__main__":
    file1 = input("Enter the first matrix file path: ")
    file2 = input("Enter the second matrix file path: ")

    matrix1 = SparseMatrix(file1)
    matrix2 = SparseMatrix(file2)

    print("\nSelect an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        result = matrix1 + matrix2
        result.save_to_file("result_add.txt")
        print("Addition result saved to result_add.txt")

    elif choice == "2":
        result = matrix1 - matrix2
        result.save_to_file("result_sub.txt")
        print("Subtraction result saved to result_sub.txt")

    elif choice == "3":
        result = matrix1 * matrix2
        result.save_to_file("result_mul.txt")
        print("Multiplication result saved to result_mul.txt")

    else:
        print("Invalid choice!")
