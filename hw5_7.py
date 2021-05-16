from json import dump

num = []
with open("hw5_7.txt", "r", encoding="utf-8") as fl_1:
    dct = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in fl_1}
    with open("hw5_7.json", "w", encoding="utf-8") as fl_2:
        for y in dct.values():
            if y > 0:
                num.append(y)
        dump([dct, {"Средняя прибыль": sum(num) / len(num)}], fl_2, ensure_ascii=False, indent=4)
