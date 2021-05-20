class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя работника: {self.name} {self.surname} ")

    def get_total_income(self):
        print("Доход с учетом премии: ", self._income["wage"] + self._income["bonus"])


w1 = Position("Иван", "Петров", "Юрист", 100000, 50000)
w1.get_full_name()
print(w1.position)
w1.get_total_income()
print()
w2 = Position("Пётр", "Иванов", "Завхоз", 10000, 80000)
w2.get_full_name()
print(w2.position)
w2.get_total_income()
