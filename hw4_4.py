from random import randint

n = int(input("Введите количетсво чисел (оптимально >= 10): "))

lst_1 = []

"""Выбран оптимальный диапазон чисел для демонстрации 1-20"""
for i in range(0, n):
    lst_1.append(randint(1, 20))

lst_2 = [i for i in lst_1 if lst_1.count(i) == 1]

print("Изначальный список: ", lst_1)
print("Конечный список уникальных элементов: ", lst_2)
