class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Машина произведена: {self.name} {self.color}, ГАИ - {self.is_police}")

    def go(self):
        print(f"{self.color} {self.name} Двигатель запущен")

    def stop(self):
        print(f"{self.color} {self.name} Двигатель остановлен")

    def turn(self, direction):
        print(f"{self.color} {self.name} Вы повернули {direction}")

    def show_speed(self):
        print(f"Ваша скорость: {self.speed}")


class TownCar(Car):

    def show_speed(self):
        print(f"{self.color} {self.name} Вы превысили скорость на: {self.speed - 60}") if self.speed > 60 else \
            print(f"{self.color} {self.name} Ваша скорость: {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f"{self.color} {self.name} Вы превысили скорость на: {self.speed - 40}") if self.speed > 60 else \
            print(f"{self.color} {self.name} Ваша скорость: {self.speed}")


class PoliceCar(Car):

    def operation(self):
        print(f"Police {self.name}. Начат план перехват.")


c1 = Car(50, "Red", "Volvo", False)
print("*" * 50)
c1.go()
c1.show_speed()
c1.turn("Налево")
c1.stop()
print("_" * 30)

c2 = TownCar(80, "Green", "Ford", False)
print("*" * 50)
c2.go()
c2.show_speed()
c2.turn("Назад")
print("_" * 30)

c4 = PoliceCar(90, "White", "UAZ", True)
print("*" * 50)
print("_" * 30)

c3 = WorkCar(79, "Orange", "KAMAZ", False)
print("*" * 50)
c3.show_speed()
c4.operation()
c3.stop()
print("_" * 30)

c5 = SportCar(160, "Blue", "McLaren", False)
print("*" * 50)
c5.go()
c5.show_speed()
c5.turn("Назад")
c5.turn("Направо")
c5.stop()
print("_" * 30)
