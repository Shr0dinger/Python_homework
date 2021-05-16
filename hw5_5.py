num = (input("Введите числа через пробел: "))

with open("hw5_5.txt", "w", encoding="utf-8") as fl:
    fl.write(num)

print("Данные записаны в файл!")

with open("hw5_5.txt", "r", encoding="utf-8") as fl_2:
    str_1 = fl_2.read()
    print("Ваши выгруженные данные", str_1)
    lst_1 = str_1.split(sep=" ")

for i in range(len(lst_1)):
    x = int(lst_1[i])
    lst_1[i] = x

print("Сумма Ваших чисел", sum(lst_1))
