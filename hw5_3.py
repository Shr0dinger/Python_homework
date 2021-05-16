sr = 0
with open("hw5_3.txt", "r", encoding="utf-8") as fl:
    str_1 = fl.readlines()
    str_2 = [i.split() for i in str_1]

for i in range(len(str_2)):
    str_3 = str_2[i]
    x = float(str_3[1])
    sr = sr + x
    if x < 20000:
        print(f"Сотрудник имеет оклад менее 20 тысяч: {str_3[0]}, зарплата сотрудника: {x}")

print("Средняя величина дохода сотрудников: ", "%.2f" % (sr / len(str_2)))
