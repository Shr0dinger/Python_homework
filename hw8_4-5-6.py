class Orgtehnika:
    def __init__(self, brand, price, year):
        self.brand = brand
        self.price = price
        self.year = year


class Printer(Orgtehnika):
    def __init__(self, brand, price, year, model, color, speed):
        super().__init__(brand, price, year)
        self.model = model
        self.color = color
        self.speed = speed
        print(f"Принтер произведен: {self.brand}, {self.model}, {self.year}, Цена - {self.price}, "
              f"Цветной - {self.color}, Скорость печати - {self.speed}")

    def Outcome(self):
        lst = [self.brand, self.model]
        print("Принтер передается на склад: ", lst)
        return lst


class Skaner(Orgtehnika):
    def __init__(self, brand, price, year, model, resolution):
        super().__init__(brand, price, year)
        self.model = model
        self.resolution = resolution
        print(f"Сканер произведен: {self.brand}, {self.model}, {self.year}, Цена - {self.price}, "
              f"Разрешение - {self.resolution}")

    def Outcome(self):
        lst = [self.brand, self.model]
        print("Сканер передается на склад: ", lst)
        return lst


class Xerox(Orgtehnika):
    def __init__(self, brand, price, year, model, color, format):
        super().__init__(brand, price, year)
        self.model = model
        self.color = color
        self.format = format
        print(f"Ксерокс произведен: {self.brand}, {self.model}, {self.year}, Цена - {self.price}, "
              f"Цветной - {self.color}, Формат - {self.format}")

    def Outcome(self):
        lst = [self.brand, self.model]
        print("Ксерокс передается на склад: ", lst)
        return lst


o_1 = Printer("Canon", 650, 2019, "T-1000", True, 20)
o_2 = Skaner("HP", 250, 2018, "ProSkan", 1200)
o_3 = Xerox("Xerox", 1100, 2020, "XRT9000", False, "A1")

print("-" * 50)


class Sklad:
    def __init__(self, count, unit):
        self.count = count
        self.unit = unit

    def Income(self):
        print(f"Наименование: {sklad_1.unit}, принято штук: {self.count}")


while True:
    try:
        name = str(input("Какую технику хотите принять на склад? Принтер, Сканер, Ксерокс? : "))
        if name == "Принтер" or name == "Сканер" or name == "Ксерокс":
            break
    except (ValueError) as err:
        print("Неверное значение наименования техники!")

if name == "Принтер":
    while True:
        try:
            count = int(input("Введите количество техники: "))
            if type(count) == int:
                break
        except (ValueError) as err:
            print("Значение должно быть числом!")
    sklad_1 = Sklad(count, o_1.Outcome())
elif name == "Сканер":
    while True:
        try:
            count = int(input("Введите количество техники: "))
            if type(count) == int:
                break
        except (ValueError) as err:
            print("Значение должно быть числом!")
    sklad_1 = Sklad(count, o_2.Outcome())
else:
    while True:
        try:
            count = int(input("Введите количество техники: "))
            if type(count) == int:
                break
        except (ValueError) as err:
            print("Значение должно быть числом!")
    sklad_1 = Sklad(count, o_3.Outcome())

print("-" * 50)

sklad_1.Income()
