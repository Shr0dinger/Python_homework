lst_1 = [7, 5, 3, 3, 2]
print("Настоящий рейинг: ", lst_1)

nmb = float(input("Введите новый элемент: "))

high = max(lst_1)
low = min(lst_1)

if nmb > high:
    lst_1.insert(0, nmb)
    print("Рейтинг с учетом Вашего числа: ", lst_1)
    quit()
elif nmb < low:
    lst_1.append(nmb)
    print("Рейтинг с учетом Вашего числа: ", lst_1)
    quit()

if lst_1.count(nmb):
    lst_1.insert(lst_1.index(nmb) + lst_1.count(nmb), nmb)
    print("Рейтинг с учетом Вашего числа: ", lst_1)

