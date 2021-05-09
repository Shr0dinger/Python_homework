lst = ["имя", "фамилия", "год рождения", "город проживания", "email", "телефон"]
dct = dict()

"""Заполнение словаря для передачи парными значениями"""
for i in range(0, len(lst)):
    dct[lst[i]] = input(f"Введите {lst[i]}: ")

"""Прием и печать данных пользователя"""


def print_func(name, sname, year, city, email, tel):
    print((f"name - {name}; sname - {sname}; year - {year}; city - {city}; email - {email}; tel - {tel}"))


print_func(name=dct[lst[0]], sname=dct[lst[1]], year=dct[lst[2]], city=dct[lst[3]], email=dct[lst[4]], tel=dct[lst[5]])
