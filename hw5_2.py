with open("hw5_2.txt", "r", encoding="utf-8") as fl:
    str_1 = fl.readlines()
    str_2 = [i.split() for i in str_1]

for i in range((len(str_2))):
    print(" ".join(str_2[i]))
    print(f"Номер строки: {i + 1}, количество слов: {len(str_2[i])} ")

print("Конец файла.")
