class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


lst = []
num = 0

while True:
    num = input("Введите число. Для завершения ввода введите 'stop': ")
    if num == "stop":
        print("Конец ввода.", lst)
        break
    else:
        try:
            lst.append(int(num))
        except (ValueError, MyOwnErr) as err:
            print(f"Разрешено вводить только числа! \n{err} \nПродолжите ввод: ")
        else:
            print(lst)
