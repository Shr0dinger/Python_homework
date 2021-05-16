trans_dict = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}

with open("hw5_4.txt", "r", encoding="utf-8") as fl_1:
    with open("hw5_4_new.txt", "w", encoding="utf-8") as fl_2:
        for i in fl_1:
            fl_2.writelines([i.replace(i.split()[0], trans_dict.get(i.split()[0]))])
