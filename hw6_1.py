import time


class TrafficLight:
    __color = None

    def running(self):
        oncolor = ('Красный', 'Желтый', 'Зеленый')
        while True:
            if TrafficLight.__color == None:
                print(f"Сейчас горит: {oncolor[0]} cвет")
                TrafficLight.__color = oncolor[0]
                time.sleep(7)
            if TrafficLight.__color == oncolor[0]:
                print(f"Сейчас горит: {oncolor[1]} cвет")
                TrafficLight.__color = oncolor[1]
                time.sleep(2)
            if TrafficLight.__color == oncolor[1]:
                print(f"Сейчас горит: {oncolor[2]} cвет")
                TrafficLight.__color = oncolor[2]
                time.sleep(5)
            if TrafficLight.__color == oncolor[2]:
                print(f"Сейчас горит: {oncolor[0]} cвет")
                TrafficLight.__color = oncolor[0]
                time.sleep(5)


a1 = TrafficLight()
a1.running()
