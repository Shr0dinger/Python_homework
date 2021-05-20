class Stationery:

    def __init__(self, title):
        self.title = title
        print(f"Инструмент создан: {self.title}")

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Pensil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


s1 = Stationery("Пишущий предмет")
s1.draw()

s2 = Pen("Ручка")
s2.draw()

s3 = Pensil("Карандаш")
s3.draw()

s4 = Handle("Маркер")
s4.draw()
