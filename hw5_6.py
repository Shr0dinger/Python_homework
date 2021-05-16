with open("hw5_6.txt", encoding="utf-8") as fl:
    for i in fl:
        num = []
        str_1 = ([y for y in i.split(" ")])
        for ii in str_1:
            num.append("".join(z for z in list(ii) if z.isdigit()))
            summ = sum([int(x) for x in num if x.isdigit()])
            name = i.split(":")[0]
        print(name, summ)
