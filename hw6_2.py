class Road:
    weight = 25
    thickness = 1 * 5

    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width

    def calc(self):
        w = (self.length * self.width * Road.weight * Road.thickness) / 1000
        print(f"Вес асфальта для указанных параметров: {w} т.")


r1 = Road(5000, 20)
r1.calc()
