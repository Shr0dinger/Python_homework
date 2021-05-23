class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return ('\n'.join(map(str, self.matrix)))

    def __add__(self, other):
        msumm = []
        for i in range(len(self.matrix)):
            msumm.append([])
            for ii in range(len(self.matrix[0])):
                msumm[i].append((self.matrix[i][ii] + other.matrix[i][ii]))
        return ('\n'.join(map(str, msumm)))


m1 = Matrix([[23, 65, 33], [99, 11, 74], [98, 19, 81]])
m2 = Matrix([[98, 19, 81], [99, 11, 74], [23, 65, 33]])
print("Матрица №1:")
print(m1)
print("Матрица №2:")
print(m2)
print("Сумма матриц:")
print(m1 + m2)
