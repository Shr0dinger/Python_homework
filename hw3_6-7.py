def int_func(wrd):
    k = " "
    rus = "абвгдеёжзиклмнопрстуфхцшщьыъэюя"

    """Проверка на наличие кириллицы в каждом слове и удаление в случае обнаружения"""
    for y in range(len(wrd)):
        for z in wrd[y]:
            k = (rus.find(z))
            if k >= 0:
                wrd[y] = " "

    for t in range(len(wrd) - 1, -1, -1):
        if wrd[t] == " ":
            del wrd[t]
    """Опереция с заглавной букве в оставшихся словах"""
    for i in range(len(wrd)):
        wrd[i] = wrd[i].title()

    return " ".join(wrd)


w = input("Введите слова латиницей с маленькой буквы: ")
w = w.split(' ')
print("Ваши слова: ", int_func(w))
