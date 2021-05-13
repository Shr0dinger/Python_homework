from itertools import count
from itertools import cycle
from sys import argv

"""На вход подаются число и слово. 
    Число определяет начальное значение генератора 
    и количество повторение элементов слова.
"""
name, x, str_1 = argv
lst_1 = [i for i in str_1]

x = int(x)
y = count(x)
z = cycle(lst_1)

for i in range(x):
    print(next(y), next(z))
