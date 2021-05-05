str_1 = input("Введите Ваши слова: ")

str_2 = str_1.split(" ")

for i, st in enumerate(str_2, 1):
    ln_str = (len(str_2[i-1]))

    if ln_str > 10:
        print(i, st[0:10])
    else:
        print(i, st)



