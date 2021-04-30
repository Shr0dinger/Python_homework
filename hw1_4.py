nmb = input("Введите Ваше число: ")
nmb_print = nmb
dl = len(nmb)
nmb = int(nmb)
i = 1
nmb_hi = 0

while i <= dl:
    nmb_x = nmb % 10
    if nmb_hi < nmb_x:
        nmb_hi = nmb_x
    nmb = nmb // 10
    i += 1

print("Ваше число: {}. Наибольшая в нём цифра: {}".format(nmb_print, nmb_hi))