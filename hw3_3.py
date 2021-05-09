lst = []
"""Заполнение списка числами от пользователя"""
for i in range(3):
    num = input(f"Введите число {i + 1}: ")
    """Если пользователь ничего не ввел"""
    if num == "":
        num = 0
    lst.insert(i, int(num))

"""Функция сложения двух наибольших чисел списка"""


def my_func(val_1, val_2, val_3):
    lst[0], lst[1], lst[2] = val_1, val_2, val_3
    y = 0
    for i in range(2):
        x = max(lst)
        lst.remove(x)
        y = int(x) + int(y)
    return int(y)


print("Сумма двух самых больших чисел: ", my_func(lst[0], lst[1], lst[2]))
