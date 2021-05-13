from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


lst_1 = [i for i in range(100, 1001, 2)]
print("Диапазон чисел: ", lst_1)
print("Произведение всех элементов диапазона: ", reduce(my_func, lst_1))
