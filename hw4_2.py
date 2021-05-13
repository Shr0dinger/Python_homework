from random import randint

n = int(input("Введите количетсво чисел: "))

lst = []

for i in range(0, n):
    lst.append(randint(1, 100))

lst_rez = [lst[y] for y in range(1, len(lst)) if lst[y] > lst[y - 1]]

print("Первоначальный список: ", lst)
print("Список чисел, больше предыдущих: ", lst_rez)
