def fact(n):
    fact = 1
    yield fact
    for i in range(2, n + 1):
        fact = fact * i
        yield fact


n = int(input("Введите число для вычисления факториала: "))

for el in fact(n - 1):
    print("Промежуточный результат: ", el)
    rez = el * n

print("Окончательный результат: ", rez)
