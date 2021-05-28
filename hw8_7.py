class Complex:

    def __init__(self, numr, numi):
        self.numr = numr
        self.numi = numi

    def __add__(self, other):
        if self.numi < 0:
            return f"Сложение комплексного числа: {self.numr + other.numr}{self.numi + other.numi}i"
        else:
            return f"Сложение комплексного числа: {self.numr + other.numr}+{self.numi + other.numi}i"

    def __mul__(self, other):
        z = self.numr * other.numi + self.numi * other.numr
        if z < 0:
            return f"Умножение комплексного числа: {self.numr * other.numr + (-(self.numi * other.numi))}" \
                   f"{self.numr * other.numi + self.numi * other.numr}i"
        else:
            return f"Умножение комплексного числа: {self.numr * other.numr + (-(self.numi * other.numi))}+" \
                   f"{self.numr * other.numi + self.numi * other.numr}i"


mc_1 = Complex(-7, -9)
mc_2 = Complex(6, -11)

print(mc_1 + mc_2)
print(mc_1 * mc_2)
