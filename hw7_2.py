from abc import ABC, abstractmethod


class Odejda(ABC):
    rez = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def summ_ras(self):
        pass

    def __add__(self, other):
        Odejda.rez += self.summ_ras + other.summ_ras
        return Cost(0)

    def __str__(self):
        x = Odejda.rez
        Odejda.rez = 0
        return f"{x}"


class Palto(Odejda):
    @property
    def summ_ras(self):
        return round(self.param / 6.5) + 0.5


class Cost(Odejda):
    @property
    def summ_ras(self):
        return round((2 * self.param + 0.3) / 100)


v = 56
h = 184
o_1 = Palto(v)
o_2 = Cost(h)
print(f"Размер пальто: {v}; Рост костюма: {h} см.")
print(f"Суммарный расход ткани: {o_1 + o_2 + o_1} м.")
