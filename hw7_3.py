class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return "\n".join(["*" * rows for i in range(self.nums // rows)]) + "\n" + "*" * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums - other.nums > 0:
            return Cell(self.nums - other.nums)
        else:
            print("Первая клетка меньше второй")

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        return Cell(self.nums // other.nums)


cell_1 = Cell(12)
cell_2 = Cell(7)
print("Увеличение клетки: ", cell_1 + cell_2)
print("Уменьшение клетки: ", cell_1 - cell_2)
print("Умножение клеток: ", cell_1 * cell_2)
print("Деление клеток: ", cell_1 // cell_2)
print("Ячейки по рядам: ")
print(cell_2.make_order(3))
