def summ():
    summ_x = 0
    ext = 0

    """Цикл с условием выхода по счетчику"""
    while ext != 1:
        lst = []
        num = input("Введите числа через пробел или q для завершения: ").split(" ")

        """Проверка на входные данные и заполнение списка"""
        for i in num:
            if num[(int(len(num)) - 1)] == "q":
                if num[0] == "q":
                    print("Конец выполнения программы")
                    ext = 1
                else:
                    print("q - ", num[(int(len(num)) - 1)])
                    num.remove("q")
                    ext = 1
            try:
                lst.append(int(i))
            except ValueError:
                print("ERROR!!")

        """Расчет и вывод суммы"""
        x = sum(lst)
        summ_x = summ_x + x
        print("Список:", lst)
        print("Сумма: ", x)
        print("Общая сумма: ", summ_x)


summ()
