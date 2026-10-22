class ArrayRowSum:
    def __init__(self):
        self.matrix = [[0 for _ in range(4)] for _ in range(4)]

    def accept(self):
        print("Enter 16 values for a 4x4 array (row-wise):")
        for i in range(4):
            for j in range(4):
                self.matrix[i][j] = int(input(f"Element [{i}][{j}]: "))

    def calculate_row_sums(self):
        for i in range(4):
            row_sum = sum(self.matrix[i])
            print(f"Sum of row {i+1}: {row_sum}")
    def display(self):
        print(self.matrix)
        self.calculate_row_sums()
        


arr = ArrayRowSum()
arr.accept()
arr.display()