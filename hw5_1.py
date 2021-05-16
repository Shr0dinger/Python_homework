"""Данные записываются каждый раз в новый файл"""

str_1 = 0
nm = input("Введите имя файла: ")
nm = nm + ".txt"

try:
    with open(nm, "x", encoding="utf-8") as fl:
        while str_1 != "":
            str_1 = input("Введите данные: ")
            print(str_1, file=fl)
            if str_1 == "":
                print(f"Запись завершена в файл: {nm}")
except IOError:
    print("Такой файл уже существует!")
