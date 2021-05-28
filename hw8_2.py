class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


num = input("Введите делимое: ")
delit = input("Введите делитель: ")

try:
    num = int(num)
    delit = int(delit)
    if delit == 0:
        raise MyOwnErr("Ошибка! Нельзя делить на 0!")
except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print("{:.3f}".format(num / delit))
finally:
    print("Программа завершена!")
